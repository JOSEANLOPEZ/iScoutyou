# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# presentación de lista
class Academic_infoAdmin(admin.ModelAdmin):
	list_display = [ 'profile', 'school', 'year_acad_graduation']
	list_per_page = 10

# presentación de lista
class Stats_infoAdmin(admin.ModelAdmin):
	list_display = [ 'profile', 'evaluations', 'sport', 'result']
	list_per_page = 10

# presentación de lista
class Video_infoAdmin(admin.ModelAdmin):
	list_display = [ 'athlete', 'video1', 'video2']
	list_per_page = 15


admin.site.register(Athlete_profile)
admin.site.register(Academic_info, Academic_infoAdmin)
admin.site.register(Stats, Stats_infoAdmin)
admin.site.register(Videos, Video_infoAdmin)
