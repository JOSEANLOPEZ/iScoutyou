from .models import *
from django import forms
from django_thumbs.db.models import ImageWithThumbsField
#from django.forms.widgets import CheckboxSelectMultiple
from .widgets import *

# Formulario de universidades
class Add_University_form(forms.ModelForm):
	class Meta:
		model = University
		fields = [

		'name',
		'division',
		'tuision_in',
		'tuition_out',
		'gpa',
		'sat',
		'act',
		'enrollement',
		'sport',
		'country',
		'state',
		'address',
		'web_page',
		'image_university'
		
		]

		labels = { 
		'sport': (''),
		'gpa': ('Min GPA'),
		'sat': ('Min SAT'),
		'act': ('ACT'),
		'image_university': (''),
		}

		widgets = { 
            'sport': ColumnCheckboxSelectMultiple(columns=4, css_class="col-xs-12 col-sm-12 col-md-3 col-lg-3"),
            'gpa': forms.NumberInput(attrs={'min': 0,  'max': 5}),
			'sat': forms.NumberInput(attrs={'min': 0,  'max': 2400}),
			'act': forms.NumberInput(attrs={'min': 0,  'max': 36}),
			'enrollement': forms.NumberInput(attrs={'min': 0}),

			
        }

        queryset = {	
        	'sport': Sport.objects.all()
        }
# frmulario de coach
class Add_Coach_form(forms.ModelForm):



	class Meta:
		model = Coach
		fields = [

			'name_coach' ,
			'email_coach' ,
			'name_assistant',
			'email_assistant' ,

		]

