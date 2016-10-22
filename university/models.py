# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from slugify import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from base.models import *
from sports.models import *

# Nombre de las diviciones 
DIVISION = (
	('D1', 'D1'),
	('D2', 'D2'),
	('D3', 'D3'),
	('NAIA', 'NAIA'),
	('NJCAA', 'NJCAA'),
)

# Pais
COUNTRY = (
	('united_states', 'United States'),
)


class University(models.Model):
	"""Modelo de universidades
	"""

	name = models.CharField(max_length=55)
	division = models.CharField(max_length=55, choices=DIVISION)
	tuision_in = models.DecimalField( validators=[MinValueValidator(0.00)], max_digits=6, decimal_places=0 )
	tuition_out = models.DecimalField( validators=[MinValueValidator(0.00)], max_digits=6, decimal_places=0 )
	gpa = models.DecimalField( validators=[MinValueValidator(0.00), MaxValueValidator(5.00)], max_digits=3, decimal_places=2 )
	sat = models.DecimalField(validators=[MinValueValidator(0.00), MaxValueValidator(2400.00)], max_digits=4, decimal_places=0)
	act = models.DecimalField( blank=True, null=True, validators=[MinValueValidator(0.00), MaxValueValidator(36.00)], max_digits=2, decimal_places=0)
	enrollement = models.DecimalField( validators=[MinValueValidator(0.00)], max_digits=5, decimal_places=0 )
	sport = models.ManyToManyField(Sport)
	country = models.CharField(max_length=45, choices=COUNTRY, default='United States' )
	state = models.ForeignKey(State)
	address = models.CharField(max_length=140)
	web_page = models.URLField()
	image_university = ImageWithThumbsField(upload_to='universityphoto',sizes=((190,240),(140,140)))

	slug        = models.SlugField(editable=False)
	
	def __unicode__(self):
		return self.name


	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(University, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Universities"


class Coach(models.Model):
	"""modelo de coach relacionados con las disiplinas de las universidades
	"""
	name_coach = models.CharField(max_length=55)
	email_coach = models.EmailField(max_length=250, blank=True, null=True)
	name_assistant = models.CharField(max_length=55, blank=True, null=True)
	email_assistant = models.EmailField(max_length=250, blank=True, null=True)
	sport = models.ForeignKey(Sport)
	university = models.ForeignKey(University)
	
	class Meta:
		verbose_name_plural = "Coaches"

