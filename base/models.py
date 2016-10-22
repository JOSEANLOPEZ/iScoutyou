# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from slugify import slugify


# Create your models here.


class State(models.Model):
	""" Modelo para guardar los estados 
	"""
	state_name = models.CharField(max_length=45)
	
	slug        = models.SlugField(editable=False)

	def __unicode__(self):
		return self.state_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.state_name)
		super(State, self).save(*args, **kwargs)


class Country(models.Model):
	""" Modelo de país
	"""
	country_name = models.CharField(max_length=45, )
	state = models.ManyToManyField(State)

	slug        = models.SlugField(editable=False)

	def __unicode__(self):
		return self.country_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.country_name)
		super(Country, self).save(*args, **kwargs)

