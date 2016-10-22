# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django_thumbs.db.models import ImageWithThumbsField
from .models import *
from .forms import *
from university.models import *
from administrator.models import *
from percent.percent import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from administrator.models import *
from django.contrib.gis.measure import Distance, D
from django.template import RequestContext
from django.views.generic.base import TemplateView
from decimal import Decimal




@login_required
def dashboard(request):
	""" Pagina Dashboar
	"""
	login = request.user
	submenu = 'academicinfo'

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:

		profile = None
		perfil = 'none'

	try:
		video1 = Videos.objects.get(athlete_id=profile.id)
		video1_self = video1.video1
		
		if video1_self == '':
			video1 = 'none'

	except:
		video1 = 'none'
		video1_self = 'none'

	try:
		video2 = video1.video2

		if video2 == '':
			video2 = 'none'
	except:
		video2 = 'none'

# Consltas

	if profile:
		stats_profile = Stats.objects.filter(profile_id = profile.id).filter(sport=profile.sport)
		acad_profile = Academic_info.objects.filter(profile_id = profile.id).order_by('-year_acad_graduation')
		coach_profile = Coaches_reference.objects.filter(profile_id = profile.id)
		athlete_history = Athlete_history.objects.filter(profile = profile.id)
		history_profile = Academic_info.objects.filter(profile_id = profile.id).order_by('-year_acad_graduation')
		club_season_history = Club_season_history.objects.filter(profile_id = profile.id).order_by('-year')
		awards = Awards.objects.filter(profile_id = profile.id).order_by('-year')
		archivement = Archivement.objects.filter(profile_id = profile.id).order_by('-year')
	else:
		perfil = 'none'

	usermail = request.user.email
	template = "dashboard.html"
	return render_to_response(template,locals())



# Editar el perfil
@login_required
def editprofile(request):
	""" Vista para editar el perfill
	"""


	submenu = 'editprofile'
 	login = request.user
	email = login.email

 	completado = percent(login)
	p = completado.calculo


 	try:
		post = Athlete_profile.objects.get(profile_user=login)
	except:
		post = None


	salvar = 'false'
	error = 'false'
	if post:

		if request.method == "POST":
			form = Editprofile_form(request.POST, request.FILES, instance=post)


			if form.is_valid():
				post = form.save(commit=False)
				post.profile_user = request.user # asignacion de usuario relacionado

				post.save()
				salvar = 'true'
				completado = percent(login)
				p = completado.calculo
				return render(request, 'form_edit_profile.html', {'email': email, 'login': login, 'form': form, 'p':p,  'submenu': submenu, 'salvar': salvar, 'error': error} )

				#return redirect(reverse('editprofile'))
			else:
				error = 'true'
		else:

			completado = percent(login)
			p = completado.calculo


			form = Editprofile_form(instance=post)


	else:

		if request.method == "POST":
			form = Editprofile_form(request.POST, request.FILES)


			if form.is_valid():
				post = form.save(commit=False)
				post.profile_user = request.user # asignacion de usuario relacionado
				post.save()
				salvar = 'true'
				submenu = 'editprofile'
				completado = percent(login)
				p = completado.calculo

			else:
				error = 'true'

		else:

			salvar = 'false'
			error = 'false'
			print (submenu)
			form = Editprofile_form()
	return render(request, 'form_edit_profile.html', {'email': email, 'login': login, 'form': form, 'p':p,  'submenu': submenu, 'salvar': salvar, 'error': error} )




@login_required
def profile_academic(request):
	""" Vista para información Academiac
	"""

	login = request.user
	email = login.email

 	completado = percent(login)
	p = completado.calculo
	submenu = 'academicinfo'


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		archivement = Archivement.objects.filter(profile_id = profile.id).order_by('-year')
		awards = Awards.objects.filter(profile_id = profile.id).order_by('-year')

	except:

		profile = None

	if profile:
		acad_profile = Academic_info.objects.filter(profile_id = profile.id).order_by('-year_acad_graduation')
	else:
		perfil = 'none'


	return render(request, 'acad_profile.html', locals())



@login_required
def delete_academic(request, id):
	""" Borrar información acadeémica
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
	email = login.email
 	completado = percent(login)
	p = completado.calculo

 	try:
		post = Academic_info.objects.get(id = id)
		select = Academic_info.objects.filter(id = id)


	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_academic')
		else:
			submenu = 'academicinfo'
			form3 = delete_acad_form(instance=post)


	else:
		submenu = 'academicinfo'

		return redirect('profile_academic')

	return render(request, 'borrar_acad.html', {'email':email,  'login':login, 'form': form3, 'submenu': submenu, 'p':p} )


@login_required
def editprofile_academic(request):
	"""Editar información academica
	"""
	login = request.user
	email = login.email
 	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form2 = Editprofile_acad_form(request.POST)
			if form2.is_valid():
				post = form2.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form2 = Editprofile_acad_form()

		return render(request, 'form_acad_edit_profile.html', {'email':email,  'login':login,'form': form2, 'submenu': submenu, 'p':p} )
	else:
		return redirect('editprofile')



@login_required
def alter_editprofile_academic(request, id):
	"""Modificar información academica
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'academicinfo'
	email = login.email

 	completado = percent(login)
	p = completado.calculo

 	try:
		post = Academic_info.objects.get(id = id)
		select = Academic_info.objects.filter(id = id)
	except:
		post = None

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form5 = Editprofile_acad_form(request.POST, instance=post)
			if form5.is_valid():
				post = form5.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form5 = Editprofile_acad_form(instance=post)

		return render(request, 'form_acad_edit_profile.html', {'email':email, 'login':login,'form': form5, 'submenu': submenu, 'p':p} )
	else:
		return redirect('editprofile')


@login_required
def editprofile_stats(request):
	""" Editar estadísticas
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None


	try:
		sport = profile.sport
	except:
		sport = None

	print (sport)

	if profile:
		if request.method == "POST":
			form3 = editprofile_measures_form(request.POST)
			if form3.is_valid():
				post = form3.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.sport = sport
				post.save()

				return redirect('profile_stats')

		else:
			submenu = 'stats'
			form3 = editprofile_measures_form()
			form3.fields["evaluations"].queryset = Evaluations.objects.filter(sport=sport)

		return render(request, 'form_stats_edit_profile.html', {'login':login,'form': form3, 'submenu': submenu, 'p':p} )
	else:
		return redirect('editprofile')



@login_required
def profile_stats(request):
	""" Información estadísticas
	"""

	login = request.user
	submenu = 'stats'

 	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:

		profile = None

	if profile:
		stats_profile = Stats.objects.filter(profile_id = profile.id)
	else:
		perfil = 'none'

	return render(request, 'stats_profile.html', locals())




@login_required
def delete_stats(request, id):
	"""Borrar información estadística
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)

 	completado = percent(login)
	p = completado.calculo
 	try:
		post = Stats.objects.get(id = id)
		select = Stats.objects.filter(id = id)

	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_stats')
		else:
			submenu = 'stats'
			form4 = editprofile_measures_form(instance=post)
	else:
		submenu = 'stats'

		return redirect('profile_stats')

	return render(request, 'borrar_stats.html', {'login':login,'form': form4, 'submenu': submenu, 'p':p} )



@login_required
def university_profile(request):
	""" Presentación de universidades en la pantalla de atletas
	"""

	login = request.user


	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if profile:
		sport =profile.sport
		gpa = profile.gpa
		sat = profile.sat


		if gpa < Decimal('2.20'):
			rango = Decimal('2.20')
			fil_university = University.objects.filter(sport=sport).filter(gpa__lte=rango ).order_by('name')
			cant_univ = fil_university.count()
			print (cant_univ)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			print('menor que 2.20')
			print (rango)
			print (gpa)
			print type(rango)
			print type(gpa)
		elif gpa >=  Decimal('2.20') and gpa <= Decimal('3.24'):
			rango = 3.25
			print('es mayor que 2.2 y menor que 3.24')
			#fil_university = University.objects.filter(sport=sport).filter(gpa__lte=gpa).filter(sat__lte=sat)
			fil_university = University.objects.filter(sport=sport).filter(gpa__lt=rango).order_by('name')
			cant_univ = fil_university.count()
			print (cant_univ)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			#print(fil_university)
			print('gpa >= 2.2 and gpa <= 3.24')
		elif gpa > Decimal('3.24'):
			fil_university = University.objects.filter(sport=sport).order_by('name')
			cant_univ = fil_university.count()
			print (cant_univ)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			print ('es mayor o igual que 3.25')


# paginacion

		page = request.GET.get('page')
		try:
			fil_university = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			fil_university = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			fil_university = paginator.page(paginator.num_pages)


	else:
		perfil = 'none'
		return render (request, 'university_profile_hide.html', locals())



	return render (request, 'university_profile.html', locals())

@login_required
def university_profile_filter(request, filtro):
	"""Presentacion de universidades aplicando los filtros
	"""


	login = request.user

	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if profile:
		# sport
		sport =profile.sport
		# GPA
		gpa = profile.gpa
		# SAT
		fsat = profile.sat


		if gpa < Decimal('2.20'):
			rango = Decimal('2.20')
			fil_university = University.objects.filter(sport=sport).filter(gpa__lte=rango ).order_by(filtro)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			cant_univ = fil_university.count()
			print (cant_univ)
			print('menor que 2.20')
			print (rango)
			print (gpa)
			print type(rango)
			print type(gpa)
		elif gpa >=  Decimal('2.20') and gpa <= Decimal('3.24'):
			rango = 3.25
			print('es mayor que 2.2 y menor que 3.24')
			#fil_university = University.objects.filter(sport=sport).filter(gpa__lte=gpa).filter(sat__lte=sat)
			fil_university = University.objects.filter(sport=sport).filter(gpa__lt=rango).order_by(filtro)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			cant_univ = fil_university.count()
			print (cant_univ)
			#print(fil_university)
			print('gpa >= 2.2 and gpa <= 3.24')
		elif gpa > Decimal('3.24'):
			fil_university = University.objects.filter(sport=sport).order_by(filtro)
			paginator = Paginator(fil_university, 25) # Show 25 contacts per page
			cant_univ = fil_university.count()
			print (cant_univ)
			print ('es mayor o igual que 3.25')


		page = request.GET.get('page')
		try:
			fil_university = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			fil_university = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			fil_university = paginator.page(paginator.num_pages)
	else:
		perfil = 'none'

	return render (request, 'university_profile.html', locals())



# ## ############################
#
# Coach
#
#
# ## ############################



@login_required
def profile_coach(request):
	""" Presentación Coach
	"""

	login = request.user
	submenu = 'coach'

 	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:

		profile = None

	if profile:
		coach_profile = Coaches_reference.objects.filter(profile_id = profile.id)
	else:
		perfil = 'none'


	return render(request, 'coach_profile.html', locals())






@login_required
def delete_coach(request, id):
	""" Borrar coach
	"""

	login = request.user

 	completado = percent(login)
	p = completado.calculo
	profile = Athlete_profile.objects.get(profile_user=login)
	prueba = Coaches_reference.objects.get(id = id)

 	try:
		post = Coaches_reference.objects.get(id = id)
		select = Coaches_reference.objects.filter(id = id)

	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_stats2')
		else:
			submenu = 'stats2'
			form10 = Editprofile_coach_form(instance=post)


	else:
		submenu = 'stats2'

		return redirect('profile_stats2')

	return render(request, 'borrar_coach.html', {'login':login,'form': form10, 'submenu': submenu, 'p':p} )







@login_required
def editprofile_coach(request):
	""" Editar Coach
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form11 = Editprofile_coach_form(request.POST)
			if form11.is_valid():
				post = form11.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form11 = Editprofile_coach_form()

		return render(request, 'form_coach_edit_profile.html', {'login':login,'form': form11, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')



@login_required
def alter_editprofile_coach(request, id):
	""" Modificar coach
	"""


	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'stats2'

 	completado = percent(login)
	p = completado.calculo

 	try:
		post = Coaches_reference.objects.get(id = id)
		select = Coaches_reference.objects.filter(id = id)

	except:
		post = None


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form12 = Editprofile_coach_form(request.POST, instance=post)
			if form12.is_valid():
				post = form12.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form12 = Editprofile_coach_form(instance=post)

		return render(request, 'form_coach_edit_profile.html', {'login':login,'form': form12, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')


@login_required
def profile_stats2(request):
	"""Editar todo el contenido de la pagina de las estadísticas del usuario 
	"""

	login = request.user
	submenu = 'stats2'
	email = login.email
 	completado = percent(login)
	p = completado.calculo


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		history_profile = Athlete_history.objects.filter(profile_id = profile.id).order_by('-year')
		coach_profile = Coaches_reference.objects.filter(profile_id = profile.id)
		club_season_history = Club_season_history.objects.filter(profile_id = profile.id).order_by('-year')
		awards = Awards.objects.filter(profile_id = profile.id).order_by('-year')
		archivement = Archivement.objects.filter(profile_id = profile.id).order_by('-year')
		prueba = Athlete_profile.objects.get(profile_user=login)


		if	profile.sport == None:

			sport = 'none'
		else:
			sport = 'true'

			sport_pos_active = Sport.objects.get(id=profile.sport.id)


			if	profile.position == None and sport_pos_active.position_act == True:

				position = 'none'

			elif profile.position == None and sport_pos_active.position_act == False:
				position = 'non_apply'

			else:
				position = 'true'

	except:
		profile = None

	if profile:
		perfil = 'true'
		if sport == 'none':
	

			if request.method == "POST":

				form_sport = Editprofile_sport_form2(request.POST, instance=profile)

				if form_sport.is_valid():

					profile = form_sport.save(commit=False)
					profile.save()
					return redirect('profile_stats2')
					sport =='true'
			else:
				submenu = 'stats2'
				sport = 'none'
				form_sport = Editprofile_sport_form(instance=profile, prueba=prueba)

			return render(request, 'stats_profile2.html', {'email':email, 'login':login, 'p':p, 'form': form_sport, 'submenu': submenu, 'sport': sport })


		elif sport == 'true' and position == 'none':
			print (position)
			print ('si no hay position then')

			if request.method == "POST":

				form_positions = Editprofile_position_form2(request.POST, instance=profile)

				if form_positions.is_valid():

					profile = form_positions.save(commit=False)
					profile.save()
					return redirect('profile_stats2')
			else:
				submenu = 'stats2'
				sport = 'true'
				form_positions = Editprofile_position_form(instance=profile, prueba=prueba)

			return render(request, 'stats_profile2.html', {'email':email, 'login':login,'p':p, 'form': form_positions, 'submenu': submenu, 'sport': sport, 'profile':profile })


		else:
			stats_profile = Stats.objects.filter(profile_id = profile.id)
			sport = profile.sport

			evaluations = Evaluations.objects.filter(sport=sport).order_by('name')

			try:
				position_eval = profile.position.id
			except:
				position_eval = 'false'

			try:
				cat_position_eval = Position.objects.filter(Q(sport_name=profile.sport) , Q(id=position_eval)) 
				cat_eval = 'false'
			except:
				cat_position_eval = 'false'
				cat_eval = Cat_evaluations.objects.filter(sport=profile.sport)


			cant = evaluations.count()

			cant_stat = stats_profile.count()

			# Stats
			stats = Stats.objects.filter(profile=profile)
			profile = Athlete_profile.objects.get(profile_user=login)

			if request.method == "POST":
				print('si hay post')
				form_sport = Athletics_form_ncaa(request.POST, instance=profile)

				print (form_sport)
				if form_sport.is_valid():

					print('es valiiiiioio')
					profile = form_sport.save(commit=False)
					profile.save()

					return redirect('profile_stats2')

			else:
				submenu = 'stats2'

				form_sport = Athletics_form_ncaa(instance=profile)

			return render(request, 'stats_profile2.html',  {'form': form_sport,
															'submenu': submenu,
															'sport': sport,
															'evaluations':evaluations,
															'history_profile':history_profile,
															'club_season_history':club_season_history,
															'coach_profile':coach_profile,
															'stats':stats,
															'perfil':perfil,
															'cat_position_eval':cat_position_eval,
															#'salvar':salvar,
															'email':email,
															'p':p,
															'login':login,
															'position':position,
															'cat_eval':cat_eval,
															})

	else:
		perfil = 'none'


	template = 'stats_profile2.html'

	return render_to_response( template, locals(), context_instance=RequestContext(request))





#----------------------------------------------

@login_required
def editprofile_stats2(request, id=0):
	"""Editar todo el contenido de la pagina de las estadísticas del usuario 
	informacion de respaldo
	"""


	login = request.user
	email = login.email
 	completado = percent(login)
	p = completado.calculo
	submenu = 'stats2'

	profile = Athlete_profile.objects.get(profile_user=login)
	acad_profile = Academic_info.objects.filter(profile_id = profile.id).order_by('-year_acad_graduation')



	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		acad_profile = Academic_info.objects.filter(profile_id = profile.id).order_by('-year_acad_graduation')

	except:

		profile = None

	if profile:
		stats_profile = Stats.objects.filter(profile_id = profile.id)
		sport = profile.sport

		# evaluations
		evaluations = Evaluations.objects.filter(sport=sport).order_by('name')

		cant = evaluations.count()


		# Stats

		stats = Stats.objects.filter(profile=profile)

	else:
		perfil = 'none'


	try:
		stat_profile =  Stats.objects.get(Q(evaluations_id=id), Q(profile=profile))

		stat_modif = stat_profile.evaluations
		stat_measure = stat_profile.evaluations.measure_name

	except:
		stat_modif = Evaluations.objects.get(id=id)
		stat_measure = 'none'






 	try:
		post = stat_profile

	except:
		post = None


	if post:

		if request.method == "POST":
			form25 = Edit_stats_form(request.POST, request.FILES, instance=post)
			print ('grabar')

			if form25.is_valid():

				post = form25.save(commit=False)
				post.profile_user = request.user # asignacion de usuario relacionado
				post.evaluations = stat_profile.evaluations
				post.sport = sport
				post.save()
				salvar = 'true'

				return redirect(reverse('profile_stats2'))
			else:
				error = 'true'
		else:

			salvar = 'false'

			form25 = Edit_stats_form(instance=post)
	else:


		if request.method == "POST":
			form25 = Edit_stats_form(request.POST, request.FILES)


			if form25.is_valid():
				post = form25.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.evaluations = stat_modif
				post.sport = sport
				post.save()
				salvar = 'true'

				return redirect(reverse('profile_stats2'))
			else:
				error = 'true'

		else:

			salvar = 'false'
			error = 'false'

			form25 = Edit_stats_form()



		form25 = Edit_stats_form()
		pass


	return render(request, 'stats_profile3.html', {'email':email, 'login':login,'p':p, 'form': form25, 'stat_modif': stat_modif,'stat_measure':stat_measure, 'evaluations':evaluations, 'stats':stats} )





@login_required
def athlete_history(request):
	""" Vista historial del athleta sin stats
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		submenu = 'stats2'
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form26 = Editprofile_history_form(request.POST)
			if form26.is_valid():
				post = form26.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form26 = Editprofile_history_form()

		return render(request, 'form_history_edit_profile.html', {'login':login,'form': form26, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')



@login_required
def athlete_history2(request):
	""" Vista historial del athleta con stats
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		submenu = 'stats2'
	except:
		profile = None


	if profile:
		hist_profile = Athlete_history.objects.filter(profile_id=profile.id)
		if not hist_profile:
			hstats_profile = Stats.objects.filter(profile_id = profile.id)
			sport = profile.sport
			sport_pos_active = Sport.objects.get(id=profile.sport.id)
			if	profile.position == None and sport_pos_active.position_act == True:
				hposition = 'none'
			elif profile.position == None and sport_pos_active.position_act == False:
				hposition = 'non_apply'
			else:
				hposition = 'true'


			hevaluations = Evaluations.objects.filter(sport=sport).order_by('name')
			try:
				hposition_eval = profile.position.id
			except:
				hposition_eval = 'false'
			try:
				hcat_position_eval = Position.objects.filter(Q(sport_name=profile.sport) , Q(id=hposition_eval)) 
				hcat_eval = 'false'
			except:
				hcat_position_eval = 'false'
				hcat_eval = Cat_evaluations.objects.filter(sport=profile.sport)

			hcant = hevaluations.count()
			hcant_stat = hstats_profile.count()
			
			# Stats
			hstats = Stats.objects.filter(profile=profile)

		if request.method == "POST":
			form26 = Editprofile_history_form(request.POST)
			if form26.is_valid():
				post = form26.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form26 = Editprofile_history_form()

		return render(request, 'form_history_edit_profile2.html', {'login':login,'form': form26, 'submenu': submenu, 'p':p, 'hcat_position_eval':hcat_position_eval, 'hposition':hposition, 'hcat_eval':hcat_eval, 'hstats':hstats} )
	else:
		return redirect('profile_stats2')




@login_required
def delete_athlete_history(request, id):
	""" Borrar historial del atleta
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
 	completado = percent(login)
	p = completado.calculo
 	try:
		post = Athlete_history.objects.get(id = id)
		select = Athlete_history.objects.filter(id = id)


	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_stats2')
		else:
			submenu = 'stats2'
			form27 = Editprofile_history_form(instance=post)


	else:
		submenu = 'stats2'

		return redirect('profile_stats2')

	return render(request, 'borrar_history.html', {'login':login,'form': form27, 'submenu': submenu, 'p':p} )



@login_required
def alter_editprofile_history(request, id):
	""" modificar historial del atleta
	"""

	login = request.user

 	completado = percent(login)
	p = completado.calculo
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'stats2'


 	try:
		post = Athlete_history.objects.get(id = id)
		select = Athlete_history.objects.filter(id = id)

	except:
		post = None


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form28 = Editprofile_history_form(request.POST, instance=post)
			if form28.is_valid():
				post = form28.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form28 = Editprofile_history_form(instance=post)

		return render(request, 'form_history_edit_profile.html', {'login':login,'form': form28, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')






@login_required
def club_season_history(request):
	""" vista club season
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		submenu = 'stats2'
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form_club = Editprofile_club_season_history_form(request.POST)
			if form_club.is_valid():
				post = form_club.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form_club = Editprofile_club_season_history_form()

		return render(request, 'form_club_season_history.html', {'login':login,'form': form_club, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')




@login_required
def delete_club_season_history(request, id):
	"""borrar club season
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)

 	completado = percent(login)
	p = completado.calculo

 	try:
		post = Club_season_history.objects.get(id = id)
		select = Club_season_history.objects.filter(id = id)


	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_stats2')
		else:
			submenu = 'stats2'
			form_del_club = Editprofile_club_season_history_form(instance=post)


	else:
		submenu = 'stats2'

		return redirect('profile_stats2')

	return render(request, 'borrar_club.html', {'login':login,'form': form_del_club, 'submenu': submenu, 'p':p} )



@login_required
def alter_editclub_season_history(request, id):
	""" Modificar club season
	"""

	login = request.user

 	completado = percent(login)
	p = completado.calculo
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'stats2'


 	try:
		post = Club_season_history.objects.get(id = id)
		select = Club_season_history.objects.filter(id = id)

	except:
		post = None


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form_edit_club = Editprofile_club_season_history_form(request.POST, instance=post)
			if form_edit_club.is_valid():
				post = form_edit_club.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_stats2')

		else:
			submenu = 'stats2'
			form_edit_club = Editprofile_club_season_history_form(instance=post)

		return render(request, 'form_club_season_history.html', {'login':login,'form': form_edit_club, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_stats2')



@login_required
def awards(request):
	""" vista award
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo

	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		submenu = 'academicinfo'
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form_award = Editprofile_award_form(request.POST)
			if form_award.is_valid():
				post = form_award.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form_award = Editprofile_award_form()

		return render(request, 'form_award.html', {'login':login,'form': form_award, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_academic')




@login_required
def delete_awards(request, id):
	"""eliminar award
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)

 	completado = percent(login)
	p = completado.calculo
 	try:
		post = Awards.objects.get(id = id)
		select = Awards.objects.filter(id = id)


	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_academic')
		else:
			submenu = 'academicinfo'
			form_del_awards = Editprofile_award_form(instance=post)


	else:
		submenu = 'academicinfo'

		return redirect('profile_academic')

	return render(request, 'borrar_awards.html', {'login':login,'form': form_del_awards, 'submenu': submenu, 'p':p} )



@login_required
def alter_editawards(request, id):
	""" Editar award
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'academicinfo'

 	completado = percent(login)
	p = completado.calculo


 	try:
		post = Awards.objects.get(id = id)
		select = Awards.objects.filter(id = id)

	except:
		post = None


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form_edit_awards = Editprofile_award_form(request.POST, instance=post)
			if form_edit_awards.is_valid():
				post = form_edit_awards.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form_edit_awards = Editprofile_award_form(instance=post)

		return render(request, 'form_award.html', {'login':login,'form': form_edit_awards, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_academic')





@login_required
def archivement(request):
	"""Vista Archivemente
	"""
	login = request.user

 	completado = percent(login)
	p = completado.calculo
	try:
		profile = Athlete_profile.objects.get(profile_user=login)
		submenu = 'academicinfo'
	except:
		profile = None

	if profile:
		if request.method == "POST":
			form_arch = Editprofile_archivement_form(request.POST)
			if form_arch.is_valid():
				post = form_arch.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form_arch = Editprofile_archivement_form()

		return render(request, 'form_archivement.html', {'login':login,'form': form_arch, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_academic')




@login_required
def delete_archivement(request, id):
	""" Borrar archivement
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)

 	completado = percent(login)
	p = completado.calculo
 	try:
		post = Archivement.objects.get(id = id)
		select = Archivement.objects.filter(id = id)


	except:
		post = None


	if post:

		if request.method == "POST":
			select.delete()
			return redirect('profile_academic')
		else:
			submenu = 'academicinfo'
			form_del_archivement = Editprofile_archivement_form(instance=post)


	else:
		submenu = 'academicinfo'

		return redirect('profile_academic')

	return render(request, 'borrar_archivement.html', {'login':login,'form': form_del_archivement, 'submenu': submenu, 'p':p} )



@login_required
def alter_editarchivement(request, id):
	""" modificar archivemente
	"""

	login = request.user
	profile = Athlete_profile.objects.get(profile_user=login)
	submenu = 'academicinfo'

 	completado = percent(login)
	p = completado.calculo

 	try:
		post = Archivement.objects.get(id = id)
		select = Archivement.objects.filter(id = id)

	except:
		post = None


	try:
		profile = Athlete_profile.objects.get(profile_user=login)
	except:
		profile = None

	if post:
		if request.method == "POST":
			form_edit_archivement = Editprofile_archivement_form(request.POST, instance=post)
			if form_edit_archivement.is_valid():
				post = form_edit_archivement.save(commit=False)
				post.profile = profile # asignacion de usuario relacionado
				post.save()

				return redirect('profile_academic')

		else:
			submenu = 'academicinfo'
			form_edit_archivement = Editprofile_archivement_form(instance=post)

		return render(request, 'form_archivement.html', {'login':login,'form': form_edit_archivement, 'submenu': submenu, 'p':p} )
	else:
		return redirect('profile_academic')
