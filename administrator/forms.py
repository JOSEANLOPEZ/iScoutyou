# -*- coding: utf-8 -*-
from .models import *
from django import forms
from django_thumbs.db.models import ImageWithThumbsField
from django.utils.safestring import mark_safe
from athletes.models import *

# Genero 
GENDER = (
	('Male', 'Male'),
	('Female', 'Female'),
	('Both', 'Both'),
)

# clases para crear los rediobuton Herizontal
class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


# CLase para agregar deportes
class Add_Sports_form(forms.ModelForm):
	class Meta:
		model = Sport
		fields = [

		'sport_name',
		'descriptions',
		'gender',
		'position_act',
		]

		labels = { 'position_act': ('It has positions'), }

		widgets = { 

  		'gender': forms.RadioSelect(choices=GENDER),
  		'position_act': forms.CheckboxInput(),
		}


# Clase para agregar posiiones
class Add_position_form(forms.ModelForm):

	class Meta:
		model = Position
		fields = [

		
		'name_positions',

		]


# Clases formulario para agregar nombre de las estadísticas
class Add_measure_form(forms.ModelForm):

	class Meta:
		model = Cat_evaluations
		fields = [

		
		'name_cat_evaluations',

		]

	

# Clase formulario de estadisticas 
class Add_stat_form(forms.ModelForm):
	class Meta:
		model = Evaluations
		fields = [


		'name',
		'measure_name',
		]

		labels = { 'measure_name': ('Unit of measure'), }


# Activar o desactivar deporte
class Act_sport_form(forms.ModelForm):

	class Meta:
		model = Sport
		fields = [

		'activate',
		]


		labels = { 'activate': "", }
		widgets = {
			'activate':forms.CheckboxInput(attrs={'style':" margin: 0 ",
														 'type':"checkbox",
														 'name':"public",
														 'class':"ui-class-checkbox",
														 'tabindex':"0",
														 'onclick':"this.form.submit();",


												 }),
		}

# Formulario de video
class Add_video_form(forms.ModelForm):

	class Meta:
		model = Videos
		fields = [

		
		'video1',
		'video2',

		]
