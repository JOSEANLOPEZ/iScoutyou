# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# presentación de lista
class Evaluation_admin(admin.ModelAdmin):
	list_display = ['sport', 'name', 'measure_name']
	list_per_page = 10

# presentación de lista
class Cat_evaluations_admin(admin.ModelAdmin):
	list_display = ['name_cat_evaluations',  'sport']
	list_per_page = 10


admin.site.register(Evaluations, Evaluation_admin)
admin.site.register(Cat_evaluations, Cat_evaluations_admin)
admin.site.register(Position)
