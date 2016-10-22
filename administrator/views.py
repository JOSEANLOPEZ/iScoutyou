# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import redirect
from athletes.models import *
from sports.models import *
from university.models import *
from .forms import *
from django.db.models import Q
from django.template import RequestContext
from percent.percent import *



def is_member(user):
	"""Funcion para validar si la persona pertenece a los usuarios administradores
	"""
	return user.groups.filter(name='administrator').exists()

@login_required
@user_passes_test(is_member)
def adm(request):
	"""Vista inicial del admin
	"""
	# Contar cuantos hay de cada uno
	users = Athlete_profile.objects.count()
	sports = Sport.objects.count()
	university = University.objects.count()

	template = "adm_dashboard.html"
	return render_to_response(template,locals())

@login_required
@user_passes_test(is_member)
def adm_sports(request):

	"""Consulta de la pagina de deportes
	"""
	sport = Sport.objects.all()
	return render (request, 'adm_sport.html', locals())

@login_required
@user_passes_test(is_member)
def add_sport(request):

	"""Vista para agregar un nuevo deporte
	"""
	if request.method == "POST":
		form = Add_Sports_form(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			
			return redirect('adm_sports')

	else:
		form = Add_Sports_form()

	return render(request, 'adm_form_add_sport.html', {'form': form} )	


@login_required
@user_passes_test(is_member)
def adm_sport_view(request, slug, id, position = 0, measure = 0, key = 0):

	"""Para vidualizar el deptalle delos deportes
	"""
	sport = Sport.objects.get(slug=slug, id=id)
	measure = int(measure)
	position = int(position)
	cat_evaluations = Cat_evaluations.objects.filter(sport_id=id)
	cat_evaluations_eval = Cat_evaluations.objects.filter(Q(sport_id=id) & Q(id=measure))
	sport_positions = Position.objects.filter(sport_name_id=sport.id)
	positions = Position.objects.filter(Q(id=position) & Q(sport_name_id=sport.id))
	positions_evaluations = Position.objects.filter(Q(id=position) & Q(sport_name_id=sport.id) & Q(cat_evaluations__id=measure))

	if positions:
		pass

	else:
		positions = 'false'

	if positions_evaluations:

		pass
	else:
		evaluation = 'false'

	if cat_evaluations and sport.position_act == False and cat_evaluations_eval:
		cat_eval = 'true'

	else:
		cat_eval = 'false'

	if request.method == "POST":
		form_act_sport = Act_sport_form(request.POST, instance=sport)
		if form_act_sport.is_valid():
			post = form_act_sport.save(commit=False)

			post.save()
			
			return redirect('adm_sport_view' , slug= slug, id= id)

	else:
		form_act_sport = Act_sport_form(instance=sport)


	template = 'adm_sport_view.html'

	return render_to_response( template, locals(), context_instance=RequestContext(request))


@login_required
@user_passes_test(is_member)
def adm_sport_edit(request, slug, id):
	"""Vista para editar deportes
	"""
	post = Sport.objects.get(slug=slug, id=id)

	if post: 

		if request.method == "POST":
			form5 = Add_Sports_form(request.POST, instance=post)
			
			if form5.is_valid():
				post = form5.save(commit=False)
				post.save()
				salvar = 'true'

			else:
				error = 'true'
		else:
			salvar = 'false'
			form5 = Add_Sports_form(instance=post)
	else:
		pass
		
	return render(request, 'adm_form_add_sport.html', {'form': form5, 'salvar': salvar, 'post':post } )



@login_required
@user_passes_test(is_member)
def add_positions(request, slug, id):
	"""Vista para agregar las posiciones
	"""
	sport = Sport.objects.get(slug=slug, id=id)

	if is_member:
		pass
	else:
		pass

	if request.method == "POST":
		form2 = Add_position_form(request.POST)
		if form2.is_valid():
			post = form2.save(commit=False)
			post.sport_name = sport
			post.save()
			
			return redirect('adm_sport_view' , slug= slug, id= id)

	else:
		form2 = Add_position_form()

	return render(request, 'adm_form_add_position.html', {'form': form2, 'sport': sport} )	



@login_required
@user_passes_test(is_member)
def add_measure(request, slug, id, positions):
	"""Agregar estadísticas
	"""
	sport = Sport.objects.get(slug=slug, id=id)
	try:
		positions = Position.objects.get(Q(sport_name=sport) & Q(id=positions))
	except:
		pass
	print(positions)


	if is_member:
		pass
	else:
		pass

	if request.method == "POST":
		form_measure = Add_measure_form(request.POST)
		if form_measure.is_valid():
			post = form_measure.save(commit=False)
			post.sport = sport
			post.save()
			if sport.position_act == True:
				positions.cat_evaluations.add(post)
				return redirect('adm_sport_view' , slug= slug, id= id, position=positions.id)
				
			else:
				return redirect('adm_sport_view' , slug= slug, id= id)

	else:
		form_measure = Add_measure_form()

	return render(request, 'adm_form_add_measure.html', {'form': form_measure, 'sport': sport, 'positions':positions} )	

 
@login_required
@user_passes_test(is_member)
def adm_athlete(request):
	"""Listado de atletas con su %
	"""

	athlete = Athlete_profile.objects.all().order_by('first_name')

	class List(list):
		def push(self, x):
			self.append(x)

	arreglo = List()

	for atletas in athlete:
	
		login = atletas.id

		completado = percent(atletas, 1)
		c = completado.calculo
		arreglo.push(c)


	dic = {}

	for dic_atletas in athlete:
		login = dic_atletas.id
		completado = percent(dic_atletas, 1)
		c = completado.calculo
		dic[int(login)] = c
		
	return render (request, 'adm_athlete.html', locals())

@login_required
@user_passes_test(is_member)
def adm_athlete_view(request, slug, id):
	"""Vista detalle del atleta
	"""


	athlete = Athlete_profile.objects.get(slug=slug, id=id)
	login = athlete.profile_user
	try:
		video1 = Videos.objects.get(athlete_id=athlete.id)

	except:
		pass
	try:
		video2 = Videos.objects.get(athlete_id=athlete.id)
	except:
		pass

	completado = percent(login)
	p = completado.calculo

	athlete_detail = Athlete_profile.objects.filter(id=id)

	template = 'adm_athlete_view.html'

	return render_to_response( template, locals(), context_instance=RequestContext(request))

	
@login_required
@user_passes_test(is_member)
def adm_athlete_view_video(request, slug, id):

	"""Vista para ver el detalle del los videos
	"""
	athlete = Athlete_profile.objects.get(slug=slug, id=id)

 	try:
		post = Videos.objects.get(athlete_id = id)
		

	except:
		post = None


	if post:
		if request.method == "POST":
			form_video = Add_video_form(request.POST, instance=post)
			if form_video.is_valid():
				post = form_video.save(commit=False)
				post.athlete = athlete # asignacion de usuario relacionado
				post.save()

				return redirect('../')

		else:

			form_video = Add_video_form(instance=post)	
	else:

		if request.method == "POST":
			form_video = Add_video_form(request.POST)
			if form_video.is_valid():
				post = form_video.save(commit=False)
				post.athlete = athlete # asignacion de usuario relacionado
				post.save()

				return redirect('../')

		else:

			form_video = Add_video_form()	

	template = 'adm_athlete_view_video.html'

	return render_to_response( template, locals(), context_instance=RequestContext(request))



@login_required
@user_passes_test(is_member)
def add_stat(request, slug, id, positions, measure):
	"""Vista de estadísticas
	"""
	sport = Sport.objects.get(slug=slug, id=id)
	measure = int(measure)
	positions = int(positions)
	positions_evaluations = Position.objects.filter(Q(id=positions) & Q(sport_name_id=sport.id) & Q(cat_evaluations__id=measure))
	cat_evaluations = Cat_evaluations.objects.get(id = measure)


	if is_member:
		pass
	else:
		pass

	if request.method == "POST":
		form2 = Add_stat_form(request.POST)
		if form2.is_valid():
			post = form2.save(commit=False)
			post.sport = sport
			post.save()
			cat_evaluations.evaluations.add(post)

			return redirect('adm_sport_view' , slug= slug, id= id, position=positions, measure=measure)

	else:
		form2 = Add_stat_form()

	return render(request, 'adm_form_add_stat.html', {'form': form2, 'sport': sport, 'measure':measure, 'positions': positions} )	
