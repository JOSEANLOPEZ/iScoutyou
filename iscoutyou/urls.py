#NO VA EN PRODUCCION
from django.conf import settings
#
from django.conf.urls import include, url
#NO VA EN PRODUCCION
from django.conf.urls.static import static
#
from django.contrib import admin
from django.contrib.auth import views as auth_views

from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

handler403 = 'base.views.custom_403_view'


urlpatterns = [
    # Admin
    url(r'^admin/$', 'administrator.views.adm', name='adm'), 
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/'}, name='salir'),
    # Admin Sport
    url(r'^admin/sports/$', 'administrator.views.adm_sports', name='adm_sports'), 
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/$', 'administrator.views.adm_sport_view', name='adm_sport_view'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<position>[0-9]+)/$', 'administrator.views.adm_sport_view', name='adm_sport_view'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<position>[0-9]+)/(?P<measure>[0-9]+)/$', 'administrator.views.adm_sport_view', name='adm_sport_view'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<position>[0-9]+)/(?P<measure>[0-9]+)/(?P<key>[0-9]+)/$', 'administrator.views.adm_sport_view', name='adm_sport_view'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/edit/$', 'administrator.views.adm_sport_edit', name='adm_sport_edit'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/positions/$', 'administrator.views.add_positions', name='add_positions'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<positions>[0-9]+)/measure$', 'administrator.views.add_measure', name='add_measure'),
    url(r'^admin/sports/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<positions>[0-9]+)/(?P<measure>[0-9]+)/stat$', 'administrator.views.add_stat', name='add_stat'),
    url(r'^admin/sports/add/$', 'administrator.views.add_sport', name='add_sport'), 

    # Admin University
    url(r'^admin/university/$', 'university.views.adm_university', name='adm_university'),
    url(r'^admin/university/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/$', 'university.views.adm_university_view', name='adm_university_view'),
    url(r'^admin/university/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<sport>[0-9]+)/$', 'university.views.adm_university_view', name='adm_university_view'),
    url(r'^admin/university/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/(?P<sport>[0-9]+)/coach/$', 'university.views.adm_university_coach_edit', name='adm_university_coach_edit'),
    url(r'^admin/university/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/edit/$', 'university.views.adm_university_edit', name='adm_university_edit'),
    url(r'^admin/university/add/$', 'university.views.add_university', name='add_university'),
    url(r'^admin/university/search/$', 'university.views.search_university', name='search_university'), 

    # Admin Athlete
    url(r'^admin/athlete/$', 'administrator.views.adm_athlete', name='adm_athlete'), 
    url(r'^admin/athlete/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/$', 'administrator.views.adm_athlete_view', name='adm_athlete_view'),
    url(r'^admin/athlete/(?P<slug>[-\w]+)/(?P<id>[0-9]+)/video/$', 'administrator.views.adm_athlete_view_video', name='adm_athlete_view_video'),

    # Super-Admin
    url(r'^superadmin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # FrontEnd atletas
    url(r'^$', 'base.views.inicio', name='inicio'), #inicio
    url(r'^accounts/$', 'base.views.accounts', name='accounts'), #inicio
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^dashboard/', 'athletes.views.dashboard', name='dashboard'),
    url(r'^editprofile/$', 'athletes.views.editprofile', name='editprofile'),
    url(r'^editprofile/academic_info/edit/$', 'athletes.views.editprofile_academic', name='editprofile_academic'),
    url(r'^editprofile/academic_info/$', 'athletes.views.profile_academic', name='profile_academic'),
    url(r'^editprofile/academic_info/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_academic', name='delete_academic'),
    url(r'^editprofile/stats/$', 'athletes.views.profile_stats', name='profile_stats'),
    url(r'^editprofile/stats/edit/$', 'athletes.views.editprofile_stats', name='editprofile_stats'),
    url(r'^editprofile/stats/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_stats', name='delete_stats'),
    url(r'^editprofile/stats/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editprofile_academic', name='alter_editprofile_academic'),
    url(r'^editprofile/colleges/$', 'athletes.views.university_profile', name='university_profile'), 
    url(r'^editprofile/colleges/filter/(?P<filtro>[-\w]+)$', 'athletes.views.university_profile_filter', name='university_profile_filter'), 
    url(r'^editprofile/colleges/(?P<universityid>[-\w]+)$', 'university.views.university', name='university'), 
    url(r'^editprofile/coach/$', 'athletes.views.profile_coach', name='profile_coach'),
    url(r'^editprofile/coach/edit/$', 'athletes.views.editprofile_coach', name='editprofile_coach'),
    url(r'^editprofile/coach/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_coach', name='delete_coach'),
    url(r'^editprofile/coach/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editprofile_coach', name='alter_editprofile_coach'),
    url(r'^editprofile/stats2/$', 'athletes.views.profile_stats2', name='profile_stats2'),
    url(r'^editprofile/stats2/edit/(?P<id>[0-9]+)$', 'athletes.views.editprofile_stats2', name='editprofile_stats2'),
    #url(r'^editprofile/athletehistory/$', 'athletes.views.athlete_history', name='athlete_history'),
    url(r'^editprofile/athletehistory/$', 'athletes.views.athlete_history2', name='athlete_history'),
    url(r'^editprofile/athletehistory/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_athlete_history', name='delete_athlete_history'),
    url(r'^editprofile/athletehistory/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editprofile_history', name='alter_editprofile_history'),
    url(r'^editprofile/club_season_history/$', 'athletes.views.club_season_history', name='club_season_history'),
    url(r'^editprofile/club_season_history/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_club_season_history', name='delete_club_season_history'),
    url(r'^editprofile/club_season_history/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editclub_season_history', name='alter_editclub_season_history'),

# ------------awards

    url(r'^editprofile/awards/$', 'athletes.views.awards', name='awards'),
    url(r'^editprofile/awards/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_awards', name='delete_awards'),
    url(r'^editprofile/awards/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editawards', name='alter_editawards'),

# -------------- archivement

    url(r'^editprofile/archivement/$', 'athletes.views.archivement', name='archivement'),
    url(r'^editprofile/archivement/delete/(?P<id>[0-9]+)/$', 'athletes.views.delete_archivement', name='delete_archivement'),
    url(r'^editprofile/archivement/(?P<id>[0-9]+)/alter/$', 'athletes.views.alter_editarchivement', name='alter_editarchivement'),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

