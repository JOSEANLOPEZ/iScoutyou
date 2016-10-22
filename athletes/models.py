# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from slugify import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from base.models import *
from sports.models import *
from administrator.models import *
from embed_video.fields import EmbedVideoField
from .pdffile import ContentTypeRestrictedFileField

from django.contrib.auth.models import User 

import datetime

year_graduation = []
year_graduation_generic = []
year_history_generic = []

for y in range(2015, (datetime.datetime.now().year + 6)):
	year_graduation.append((y, y))

for y in reversed (range(2009, (datetime.datetime.now().year + 1))):
	year_graduation_generic.append((y, y))

for y in range(2010, (datetime.datetime.now().year + 1)):
	year_history_generic.append((y, y))


PARENTS = (
	('Mother', 'Mother'),
	('Father', 'Father'),
)

GUARDIAN = (

	('Coach', 'Coach'),
	('Manager', 'Manager'),
	('Mother', 'Mother'),
	('Father', 'Father'),
)

COUNTRY = (
	('united_states', 'United States'),
)

YEARS = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
)


class Athlete_profile(models.Model):
	""" Perfil del Athleta
	Se crea cuando el athleta carga su información básica, el atleta debe tener un usuario en :model:`auth.User`.
	"""
	profile_user = models.OneToOneField(User, unique=True)

# General information
	first_name = models.CharField(max_length=35)
	middle_name = models.CharField(max_length=35, blank=True, null=True )
	last_name = models.CharField(max_length=35)
	birth = models.DateField(blank=True, null=True)
	gender = models.CharField(max_length=8 , blank=True, null=True)
	address = models.CharField(max_length=140)
	address2 = models.CharField(max_length=140)
	image_profile = ImageWithThumbsField(upload_to='profilephoto',sizes=((190,240),(140,140)) )
	state = models.ForeignKey(State)
	country = models.CharField(max_length=45, choices=COUNTRY, default='United States' )
	ncaa = models.CharField(max_length=11, blank=True, null=True)

# Contact Information
	home_phone = models.CharField(max_length=16)
	cel_phone = models.CharField(max_length=16)
# Guardian 1 Information
	guardian1 = models.CharField(max_length=25, choices=PARENTS)
	g_first_name = models.CharField(max_length=35)
	g_last_name = models.CharField(max_length=35)
	g_phone = models.CharField(max_length=16)
	g_mail = models.EmailField(max_length=250)
# Guardian 2 Information

	guardian2 = models.CharField(max_length=25, choices=GUARDIAN, blank=True, null=True)
	g2_first_name = models.CharField(max_length=35, blank=True, null=True)
	g2_last_name = models.CharField(max_length=35, blank=True, null=True)
	g2_phone = models.CharField(max_length=16, blank=True, null=True)
	g2_mail = models.EmailField(max_length=250, blank=True, null=True)


# Academic Files
	gpa = models.DecimalField( validators=[MinValueValidator(0.00), MaxValueValidator(5.00)], max_digits=3, decimal_places=2 )
	sat = models.DecimalField( blank=True, null=True,  validators=[MinValueValidator(0.00), MaxValueValidator(2400.00)], max_digits=4, decimal_places=0)
	act = models.DecimalField( blank=True, null=True,  validators=[MinValueValidator(0.00), MaxValueValidator(36.00)], max_digits=2, decimal_places=0)
	gpa_pdf = ContentTypeRestrictedFileField(upload_to='pdf/gpa', content_types=['application/pdf', 'image/jpeg'], max_upload_size=10485760, blank=True, null=True)
	sat_pdf = ContentTypeRestrictedFileField(upload_to='pdf/sat', content_types=['application/pdf', 'image/jpeg'], max_upload_size=10485760, blank=True, null=True)
	act_pdf = ContentTypeRestrictedFileField(upload_to='pdf/act', content_types=['application/pdf', 'image/jpeg'], max_upload_size=10485760, blank=True, null=True)
	hs_grad_year = models.IntegerField(('year'), max_length=4, choices=year_graduation, default=datetime.datetime.now().year)
	sport = models.ForeignKey(Sport,  null=True)
	position = models.ForeignKey(Position, null=True)
	personal_statement = models.TextField(blank=True)
	varsity_yn = models.CharField(max_length=3 , blank=True, null=True)
	varsity_club = models.CharField(blank=True, null=True, max_length=55)
	varsity_years = models.CharField(max_length=1 , blank=True, null=True, choices = YEARS)
	weight = models.DecimalField( blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(250)], max_digits=3, decimal_places=0)
	height = models.CharField( blank=True, null=True, max_length=10)
	slug  = models.SlugField(editable=False)

	def __unicode__(self):
		return self.profile_user.email

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(unicode(self.profile_user.email))
		super(Athlete_profile, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural='Athlete Profile'


class Academic_info(models.Model):
	""" Modelo de la información académica logros
	"""
	year_acad_graduation = models.IntegerField(('year'), max_length=4, choices=year_graduation_generic, default=datetime.datetime.now().year)
	school = models.CharField(max_length=140)
	logros = models.CharField(max_length=300) 
	profile = models.ForeignKey(Athlete_profile)

	class Meta:
		verbose_name_plural = "Academic Info" 	
	

class Videos(models.Model):
	""" Tabla de los videos del atleta
	"""
	athlete = models.ForeignKey(Athlete_profile)
	video1 = EmbedVideoField("Video 1",blank=True, null=True)
	video2 = EmbedVideoField("Video 2",blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "Videos"


class Stats(models.Model):
	""" Modelo estadísticas del atleta
	Modelo donde se guardan las estadísticas del atleta deacuerdo con el deporte 
	"""	
	profile = models.ForeignKey(Athlete_profile)
	evaluations = models.ForeignKey(Evaluations)
	sport = models.ForeignKey(Sport)
	result = models.CharField(max_length=45)

	class Meta:
		verbose_name_plural = "Stats"

class Coaches_reference(models.Model):
	""" Modelo donde se cuardan información de los coach
	"""	
	coach_name = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	phone = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField(max_length=250, blank=True, null=True)
	profile = models.ForeignKey(Athlete_profile)

	def __unicode__(self):
		return self.coach_name

class Athlete_history(models.Model):
	""" Modelo de información del atleta
	"""
	year = models.IntegerField(('year'), max_length=4, choices=year_history_generic, default=datetime.datetime.now().year)
	highschool = models.CharField(max_length=55)
	descriptions = models.CharField(max_length=100)
	profile = models.ForeignKey(Athlete_profile)

class History_stats(models.Model):
    	""" Modelo estadísticas por historia del atleta
	Modelo donde se guardan las estadísticas por año de hisotoria del atleta deacuerdo con el deporte 
	"""	
	profile = models.ForeignKey(Athlete_profile)
	evaluations = models.ForeignKey(Evaluations)
	sport = models.ForeignKey(Sport)
	history = models.ForeignKey(Athlete_history)
	result = models.CharField(max_length=45)

	class Meta:
		verbose_name_plural = "History_Stats"


class Club_season_history(models.Model):
	""" Modelo del CLub season history
	"""
	year = models.IntegerField(('year'), max_length=4, choices=year_history_generic, default=datetime.datetime.now().year)
	club = models.CharField(max_length=55)
	descriptions = models.CharField(max_length=100)
	profile = models.ForeignKey(Athlete_profile)


class Awards(models.Model):
	""" Modelo de los logros del atleta
	"""
	year = models.IntegerField(('year'), max_length=4, choices=year_history_generic, default=datetime.datetime.now().year)
	awards = models.CharField(max_length=55)
	descriptions = models.CharField(max_length=100)
	profile = models.ForeignKey(Athlete_profile)

class Archivement(models.Model):
	"""Modelo Archivement
	"""
	year = models.IntegerField(('year'), max_length=4, choices=year_history_generic, default=datetime.datetime.now().year)
	#archivement = models.CharField(max_length=55)
	descriptions = models.CharField(max_length=100)
	profile = models.ForeignKey(Athlete_profile)

		
