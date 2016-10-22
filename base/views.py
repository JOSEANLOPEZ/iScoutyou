from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def inicio(request):
	""" redideccion edit profile
	"""
    
	return HttpResponseRedirect("/editprofile/")

@login_required
def accounts(request):
	"""redireccion cuentas de usuario
	"""

	template = "accounts.html"
	return render_to_response(template,locals())



def custom_403_view(request):
	template = 'custon_403.html'
	return render_to_response(template, locals())

 