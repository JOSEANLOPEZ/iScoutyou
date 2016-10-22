from django.contrib import admin
from .models import *

class Sport_admin(admin.ModelAdmin):
	list_display = [ 'sport_name', 'position_act', 'gender']
	list_per_page = 15


admin.site.register(Sport, Sport_admin)

