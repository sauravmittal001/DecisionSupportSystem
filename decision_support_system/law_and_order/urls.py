from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # static pages
    url(r'^$', views.index, name='index'),
    url(r'^home.html$', views.home, name='home'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^new_event.html', views.new_event, name='new_event'),

    # event tables
    url(r'^rally.html$', views.rally, name='rally'),
    url(r'^crime.html$', views.crime, name='crime'),
    url(r'^epidemic.html$', views.epidemic, name='epidemic'),
    url(r'^natural_calamities.html$', views.natural_calamities, name='natural_calamities'),
    url(r'^public_gathering.html$', views.public_gathering, name='public_gathering'),

    # API
    url(r'^epidemic', views.EpidemicDetail.as_view()),
    url(r'^epidemic/(?P<pk>\d+)/$', views.EpidemicDetail.as_view(), name='update event'),
    url(r'^epidemic', views.EpidemicDetail.as_view(), name='delete_event'),

    url(r'^publicGathering', views.PublicGatheringDetail.as_view()),
    url(r'^publicGathering/(?P<pk>\d+)/$', views.PublicGatheringDetail.as_view(), name='update event'),
    url(r'^publicGathering', views.PublicGatheringDetail.as_view(), name='delete_event'),

    url(r'^rally', views.RallyDetail.as_view()),
    url(r'^rally/(?P<pk>\d+)/$', views.RallyDetail.as_view(), name='update event'),
    url(r'^rally', views.RallyDetail.as_view(), name='delete_event'),

    url(r'^crime', views.CrimeDetail.as_view()),
    url(r'^crime/(?P<pk>\d+)/$', views.CrimeDetail.as_view(), name='update event'),
    url(r'^crime', views.CrimeDetail.as_view(), name='delete_event'),

    url(r'^naturalCalamities', views.NaturalCalamitiesDetail.as_view()),
    url(r'^naturalCalamities/(?P<pk>\d+)/$', views.NaturalCalamitiesDetail.as_view(), name='update event'),
    url(r'^naturalCalamities', views.NaturalCalamitiesDetail.as_view(), name='delete_event'),

    # model forms
    url(r'^new_event_rally.html', views.rallyform),
    url(r'^new_event_crime.html', views.crimeform),
    url(r'^new_event_epidemic.html', views.epidemicform),
    url(r'^new_event_natural_calamities.html', views.naturalcalamitiesform),
    url(r'^new_event_public_gathering.html', views.publicgatheringform),

]

urlpatterns = format_suffix_patterns(urlpatterns)
