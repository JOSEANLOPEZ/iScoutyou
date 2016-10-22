# -*- coding: utf-8 -*-
from .models import *
from django import forms
from django_thumbs.db.models import ImageWithThumbsField
from .models import *
from .views import *
from django.db.models import Q

GENDER = (
	('Male', 'Male'),
	('Female', 'Female'),
)

YN = (
	('Yes', 'Yes'),
	('No', 'No'),
)

# Formulario para editar el perfil del atleta
class Editprofile_form(forms.ModelForm):


	class Meta:
		model = Athlete_profile
		fields = [

		'first_name',
		'middle_name',
		'last_name',
		'birth',
		'gender',
		'weight',
		'height',
		'image_profile',
		'address',
		'address2',
		'country',
		'state',
		'ncaa',
		'home_phone',
		'cel_phone',
		'guardian1',
		'g_first_name',
		'g_last_name',
		'g_phone',
		'g_mail',
		'guardian2',
		'g2_first_name',
		'g2_last_name',
		'g2_phone',
		'g2_mail',
		'gpa',
		'gpa_pdf',
		'sat',
		'sat_pdf',
		'act',
		'act_pdf',
		'hs_grad_year',
		#'sport',
		'personal_statement',

		]

  		labels = {
  			'home_phone':('Phone'),
			'cel_phone':('Mobile'),
			'image_profile':(''),
        	'address': ('Address line 1'),
        	'address2': ('Address line 2'),
        	'guardian1': ('select'),
			'g_first_name': ('First name'),
			'g_last_name': ('Last name'),
			'g_phone': ('Mobile'),
			'g_mail': ('Email'),
			'guardian2': ('select'),
			'g2_first_name': ('First name'),
			'g2_last_name': ('Last name'),
			'g2_phone': ('Mobile'),
			'g2_mail': ('Email'),
			'personal_statement': (''),
			'hs_grad_year': ('Graduation Year'),
			'gpa_pdf':(''),
			'sat_pdf':(''),
			'act_pdf':(''),
        }


		widgets = {

			'cel_phone':forms.TextInput(attrs={'class':"phone_with_ddd"}),
			'home_phone':forms.TextInput(attrs={'class':"phone_with_ddd"}),
			'first_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'middle_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'last_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'gender': forms.RadioSelect(choices=GENDER),
            'birth': forms.TextInput(attrs={'readonly':True}),
            'address': forms.TextInput(attrs={'pattern':"[a-zA-Z0-9?:\d*\.\,\(\)\*\+\-\.\/\\s]+", 'class': "alphanumber", 'data-toggle': "tooltip", 'title': "Street address, apartment, suite, unit, building, floor, etc", 'placeholder': "Street address, apartment, suite, unit, building, floor, etc"}),
            'address2': forms.TextInput(attrs={'pattern':"[a-zA-Z0-9?:\d*\.\,\(\)\*\+\-\.\/\\s]+",'class': "alphanumber", 'data-toggle': "tooltip", 'title': "City, Province/Region, Zip", 'placeholder': "City, Province/Region, Zip"}),
            'ncaa': forms.TextInput(attrs={'class': "ncaa",  'placeholder': "NCAA ID", }),
			'gpa': forms.NumberInput(attrs={'min': 0,  'max': 5}),
			'sat': forms.NumberInput(attrs={'min': 0,  'max': 2400}),
			'g2_first_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'g2_last_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'g_first_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'g_last_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'g2_phone':forms.TextInput(attrs={'class':"phone_with_ddd"}),
			'g_phone':forms.TextInput(attrs={'class':"phone_with_ddd"}),
			'image_profile': forms.FileInput(attrs={'class':"upload", 'id': "uploadBtn"}),
			'weight':forms.TextInput(attrs={'class': "weight",  'placeholder': "000 lbs"}),
			'height':forms.TextInput(attrs={'class': "hei", 'placeholder': "0'00'' feet, inches"}),
			'pdf_GPA': forms.FileInput(attrs={'class':"upload", 'id': "uploadBtnGPA"}),
			'pdf_SAT': forms.FileInput(attrs={'class':"upload", 'id': "uploadBtnSAT"}),
			'pdf_ACT': forms.FileInput(attrs={'class':"upload", 'id': "uploadBtnACT"}),
			'personal_statement':forms.Textarea(attrs={'pattern':"[a-zA-Z0-9\\s]+", 'class': "alphanumber"})
        }

# Formulario información académica
class Editprofile_acad_form(forms.ModelForm):


	class Meta:
		model = Academic_info
		fields = [


		'year_acad_graduation',
		'school',
		#'logros',

		]

		labels = {
		'school': ('High School'),
		'year_acad_graduation': ('Graduation Year'),
		}


# Formulario borrar información acadéica
class delete_acad_form(forms.ModelForm):

	class Meta:
		model = Academic_info

		fields = [


		'year_acad_graduation',
		'school',


		]

		labels = {
		'school': ('High School'),
		'year_acad_graduation': ('Graduation Year'),
		}

# Formulario editar estdísticas
class editprofile_measures_form(forms.ModelForm):

	class Meta:
		model = Stats

		fields = [

		'evaluations',
		'result',

		]



# ## ############################
#
# Coach
#
#
# ## ############################

class Editprofile_coach_form(forms.ModelForm):


	class Meta:
		model = Coaches_reference
		fields = [

		'coach_name',
		'position',
		'phone',
		'email',

		]

		labels = { 
		'coach_name': ('Name'),
		'phone': ('Mobile'),
		 }

		widgets = {

			'coach_name': forms.TextInput(attrs={'pattern':"[a-zA-Z\\s]+", 'class': "alpha"}),
			'phone':forms.TextInput(attrs={'class':"phone_with_ddd"}),

			
        }

# borrar coach
class delete_coach_form(forms.ModelForm):

	class Meta:
		model = Coaches_reference

		fields = [

		'coach_name',
		'position',
		'phone',
		'email',

		]

		labels = { 'coach_name': ('Name'), }


# editar stats
class Edit_stats_form(forms.ModelForm):

	class Meta:
		model = Stats
		fields = [

		'result',
		]

# formulario History profile
class Editprofile_history_form(forms.ModelForm):
	class Meta:
		model = Athlete_history
		fields = [

		'year',
		'highschool',
		'descriptions',


		]

		widgets = {

		}


#Formulario deportes profile
class Editprofile_sport_form(forms.ModelForm):


	def __init__(self, prueba, *args, **kwargs):

		super(Editprofile_sport_form, self).__init__(*args, **kwargs)

		self.fields['sport'].queryset = Sport.objects.filter(Q(gender=prueba.gender) | Q(gender='Both'), activate=True )
		
		
	class Meta:
		model = Athlete_profile
		fields = [

		'sport',

		]

# formulario deportes respaldo 
class Editprofile_sport_form2(forms.ModelForm):


	class Meta:
		model = Athlete_profile
		fields = [


		'sport',

		]

# formulario editar posición 
class Editprofile_position_form(forms.ModelForm):


	def __init__(self, prueba, *args, **kwargs):

		super(Editprofile_position_form, self).__init__(*args, **kwargs)

		self.fields['position'].queryset = Position.objects.filter(Q(sport_name=prueba.sport) )

	class Meta:
		model = Athlete_profile
		fields = [


		'position',

		]

# formulario editar posición respaldo 
class Editprofile_position_form2(forms.ModelForm):



	class Meta:
		model = Athlete_profile
		fields = [


		'position',

		]

# formulario club_season_history

class Editprofile_club_season_history_form(forms.ModelForm):
	class Meta:
		model = Club_season_history
		fields = [

		'year',
		'club',
		'descriptions',


		]


		widgets = {

		}


# Formulario awards

class Editprofile_award_form(forms.ModelForm):
	class Meta:
		model = Awards
		fields = [

		'year',
		'awards',
		'descriptions',


		]


		widgets = {

		}

# formaulario archivement

class Editprofile_archivement_form(forms.ModelForm):
	class Meta:
		model = Archivement
		fields = [

		'year',

		'descriptions',


		]


		widgets = {

		}


# Formulrio ncaa
class Athletics_form_ncaa(forms.ModelForm):


	class Meta:
		model = Athlete_profile
		fields = [

		'varsity_yn',
		'varsity_club',
		'varsity_years',

		]

  		labels = {

        	'varsity_yn':(''),
        	'varsity_club': ('Club'),
			'varsity_years': ('Years') ,
        }


		widgets = {

			'varsity_yn': forms.RadioSelect(choices=YN),
        }
