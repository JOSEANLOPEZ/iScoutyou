# -*- coding: utf-8 -*-
from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from slugify import slugify
from administrator.models import *


class Sport(models.Model):
	""" Modelo Deportes
	Se pueden activar o desactivar
	"""
	sport_name = models.CharField(max_length=45)
	descriptions = models.TextField(max_length=300)
	position_act = models.BooleanField(default=True)
	gender = models.CharField(max_length=8)
	slug = models.SlugField(editable=False)
	activate = models.BooleanField(default=False)

	def __unicode__(self):
		return self.sport_name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.sport_name)
		super(Sport, self).save(*args, **kwargs)


