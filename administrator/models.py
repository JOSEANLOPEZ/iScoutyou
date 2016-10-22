# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from slugify import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from base.models import *
from sports.models import *



class Evaluations(models.Model):

	""" Nombre las estadísticas por deportes
	nombre de la estádistica y unidad de edida
	"""
	sport = models.ForeignKey(Sport)
	name = models.CharField(max_length=45)
	measure_name = models.CharField(max_length=45)

	slug        = models.SlugField(editable=False)
	
	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Evaluations, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Evaluations"


class Cat_evaluations(models.Model):
	""" Nombre del grupo de estadísticas que corresponden al deporte
	"""
	name_cat_evaluations = models.CharField(max_length=45)
	evaluations = models.ManyToManyField(Evaluations, blank=True, null=True)
	sport = models.ForeignKey(Sport)

	def __unicode__(self):
		return self.name_cat_evaluations

	class Meta:
		verbose_name_plural = "Cat Evaluations"


class Position(models.Model):
	""" Posiciones del deporte
	relacionadas con cada deporte
	"""
	name_positions = models.CharField(max_length=55)
	sport_name =  models.ForeignKey(Sport)
	cat_evaluations = models.ManyToManyField(Cat_evaluations, blank=True, null=True)

	def __unicode__(self):
		return self.name_positions
