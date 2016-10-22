from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import redirect
from athletes.models import *
from sports.models import *
from university.models import *
from .forms import *
from django.db.models import Q
from percent.percent import *
from administrator.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def is_member(user):
    return user.groups.filter(name='administrator').exists()


@login_required
@user_passes_test(is_member)
def adm_university(request):
	"""Vista de universidades
	"""

	university = University.objects.all().order_by('name')
	
	cant_univ = university.count()

	paginator = Paginator(university, 20) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		university = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		university = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		university = paginator.page(paginator.num_pages)


	return render (request, 'adm_university.html', locals())


@login_required
@user_passes_test(is_member)
def search_university(request):
	#Vista de universidades con busqueda

    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) |
            Q(coach__name_coach__icontains=query) |
            Q(coach__name_assistant__icontains=query)
        )
        results = University.objects.filter(qset).distinct().order_by('name')
    elif not query:
    	results = University.objects.all().order_by('name')


	university = results	
	cant_univ = results.count()
	print(cant_univ)
	paginator = Paginator(university, 20) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		university = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
		university = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
		university = paginator.page(paginator.num_pages)

    return render_to_response("adm_search.html", locals())




@login_required
@user_passes_test(is_member)
def adm_university_view(request, slug, id, sport=0):
	""" Vista detalle de universidades
	"""

	university = University.objects.get(slug=slug, id=id)

	univ_detail = University.objects.filter(id=id)
	coach = Coach.objects.filter(university=university, sport=sport)
	sport = int(sport)

	if sport == 0:
		pass
	else:
		try:
			coach = Coach.objects.get(university=university, sport=sport)
			print(coach.name_coach)
		except:
			pass



	template = 'adm_university_view.html'

	return render_to_response( template, locals())

@login_required
@user_passes_test(is_member)
def add_university(request):
	""" vista para agregar universidades
	"""

	if request.method == "POST":
		form3 = Add_University_form(request.POST)
		if form3.is_valid():
			post = form3.save(commit=False)
			post.save()
			form3.save()
			
			return redirect('adm_university')

	else:
		
		form3 = Add_University_form()

	return render(request, 'adm_form_add_university.html', {'form': form3} )	





@login_required
@user_passes_test(is_member)
def adm_university_edit(request, slug, id):
	""" Vista para editar universidades
	"""
	post = University.objects.get(slug=slug, id=id)

	if post: 
		print("si hay post")

		if request.method == "POST":
			form4 = Add_University_form(request.POST, request.FILES, instance=post)
			print ('grabar')
			
			if form4.is_valid():
				post = form4.save(commit=False)
				post.save()
				form4.save_m2m()
				salvar = 'true'

				return redirect('../')
			else:
				error = 'true'
		else:

			salvar = 'false'

			form4 = Add_University_form(instance=post)
	else:
		print("no hay")

	
		
	return render(request, 'adm_form_add_university.html', {'form': form4, 'salvar': salvar, 'post':post} )



@login_required
@user_passes_test(is_member)
def adm_university_coach_edit(request, slug, id, sport):
	""" vista coach por universida
	"""

	university = University.objects.get(slug=slug, id=id)
	sports = Sport.objects.get(id = sport)

	try:
		post = Coach.objects.get(university=university.id, sport__id=sport)


	except:
		post = None


	if post: 


		if request.method == "POST":
			form_coach = Add_Coach_form(request.POST, request.FILES, instance=post)

			
			if form_coach.is_valid():
				post = form_coach.save(commit=False)
				post.sport_id = sports
				post.university__id = id
				post.save()

				return redirect('../')
			else:
				error = 'true'
		else:

			salvar = 'false'

			form_coach = Add_Coach_form(instance=post)
	else:
		print("no hay post")
		if request.method == "POST":
			form_coach = Add_Coach_form(request.POST)
			print ('grabar')

			if form_coach.is_valid():
				post = form_coach.save(commit=False)
				post.sport_id = sport
				post.university_id = id
				post.save()

				return redirect('../')
			else:
				error = 'true'
		else:

			salvar = 'false'

			form_coach = Add_Coach_form()

	
		
	return render(request, 'adm_form_add_coach.html', {'form': form_coach, 'salvar': salvar, 'post':post} )


@login_required
def university(request, universityid=0):
	""" univerdisdes selecionada
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)

	print (login)


 	completado = percent(login)
	p = completado.calculo

	sport =profile.sport
	# GPA
	gpa = profile.gpa
	# SAT
	sat = profile.sat

	if sat > 0:
		try:

			university = University.objects.get(Q(id = universityid), Q(sport=sport), Q(gpa__lte=gpa) | Q(sport=sport), Q(sat__lte=sat))
			print (university)
			print('mayor que cero')
		except:
			pass
	else:
		try:
			university = University.objects.get(Q(id = universityid), Q(sport=sport), Q(gpa__lte=gpa))
			print(university)
			print ('menor que cero')
		except:
			pass

	try:

		coach = Coach.objects.get(university = university.id, sport = profile.sport.id)
		print (coach.name_coach)
		print(university)
	except:
		print('no hay university')

	template = 'university.html'
	return render_to_response( template, locals())