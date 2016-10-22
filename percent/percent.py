from django.db import models
from django.contrib.auth import *

from administrator.models import *
from athletes.models import *
from sports.models import *
from university.models import *

# Clase para el calculo del porcentaje
# 
class percent(object):


	def __init__(self, login, admin = 0):
		print 'holaaa'
		
		self.usuario = login

		try:
			self.perfil_atleta = Athlete_profile.objects.get(profile_user=self.usuario)

		except:
			self.perfil_atleta = 'none'

		try:

			if admin == 1:
				self.perfil_atleta = Athlete_profile.objects.get(id=self.usuario.id)
			self.usuario.email = 'true'

		except:
			pass

		if self.perfil_atleta == 'none':

			self.calculo = 0
			
		else:

			self.acad_info = Academic_info.objects.filter(profile_id=self.perfil_atleta.id)
			

			stats_profile = Stats.objects.filter(profile_id = self.perfil_atleta.id)

			evaluations = Evaluations.objects.filter(sport_id=self.perfil_atleta.sport)

			try:
				self.video = Videos.objects.get(athlete_id = self.perfil_atleta.id )

				if self.video.video1 == '':
					pass

			except:
				self.video = 0
				pass

			self.stats = stats_profile.count()
			self.eval = evaluations.count()

# los print son importantes para hacer debug por consola 
# 
			self.calculo = 0
			if self.perfil_atleta.first_name:

				self.calculo = 5
				print('calculo + 5 = ', self.calculo)
			else:
				print('no tiene first_name 5')



			if self.perfil_atleta.last_name:
				self.calculo = self.calculo + 5
				print('si tiene_last 5')
				print('calculo + 5 = ', self.calculo)
				
			else:
				print('no tiene last_name 5')


			if self.perfil_atleta.home_phone:
				self.calculo = self.calculo + 5
				print('si tiene home_phone 5')
				print('calculo + 5 = ', self.calculo)
			else:
				print('no tiene home_phone 5')				

			if self.video == 0 or self.video.video1 == '':
				print('no tiene video 20')
				print(self.calculo)
		
			else:
				self.calculo = self.calculo + 20
				print('si tiene video 20')
				print(self.calculo)
				print('calculo + 20 = ', self.calculo)

				
			if self.perfil_atleta.cel_phone:
				self.calculo = self.calculo + 5
				print('si tiene cel_phone 5')
				print('calculo + 5 = ', self.calculo)
			else:
				print('no tiene cel_phone 5')
				
			if self.usuario.email:
				self.calculo = self.calculo + 5
				print('si tiene email 5')
				print('calculo + 5 = ', self.calculo)
			else:
				print('no tiene email 5')

			if self.perfil_atleta.country:
				self.calculo = self.calculo + 2
				print('si tiene country 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene country 2')

			if self.perfil_atleta.hs_grad_year:
				self.calculo = self.calculo + 2
				print('si tiene year gradue 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene year gradue 2')
			
			if self.perfil_atleta.state:
				self.calculo = self.calculo + 2
				print('si tiene state 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene state 2')

			if self.perfil_atleta.birth:
				self.calculo = self.calculo + 2
				print('si tiene birth 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene birth 2')

			if self.perfil_atleta.address:
				self.calculo = self.calculo + 2
				print('si tiene addres 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene addres 2')

			if self.perfil_atleta.image_profile:
				self.calculo = self.calculo + 2
				print('si tiene image 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene image 2')
			
			if self.perfil_atleta.sport:
				self.calculo = self.calculo + 5	
				print('si tiene sport 5')
				print('calculo + 5 = ', self.calculo)
			else:
				print('no tiene sport 5')

			if self.perfil_atleta.ncaa:
				print(self.perfil_atleta.ncaa)
				self.calculo = self.calculo + 2	
				print('si tiene ncaa 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene ncaa 2')
				print(self.perfil_atleta.ncaa)



			if self.perfil_atleta.gpa:
				self.calculo = self.calculo + 15
				print('si tiene gpa 15')
				print('calculo + 15 = ', self.calculo)
			else:
				print('no tiene gpa 15')

			if self.acad_info:
				self.calculo = self.calculo + 2
				print('si tiene acad_info 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene acad_info 2')

			if self.stats == self.eval & self.eval != 0:
				self.calculo = self.calculo + 15
				print('si tiene stats 15')
				print('calculo + 15 = ', self.calculo)
			else:
				print('no tiene stats 15')


			if self.perfil_atleta.g_first_name:
				self.calculo = self.calculo + 2
				print('si tiene g_name 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene g_name 2')

			if self.perfil_atleta.g2_first_name:
				self.calculo = self.calculo + 2
				print('si tiene g2_name 2')
				print('calculo + 2 = ', self.calculo)
			else:
				print('no tiene g2_name 2')


			
class percent2(object):

	def __init__(self, athlete):
		print ('percent2')
		self.atletas = athlete

	def calcular(self, *args, **kwargs):
		prueba = self.atletas

		pass


