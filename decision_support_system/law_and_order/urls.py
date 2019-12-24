from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^testApi$', views.apiTest, name='apiTest'),
    url(r'^home.html$', views.home, name='home'),
    url(r'^critical_route.html$', views.critical_route, name='critical_route'),
    url(r'^riots.html$', views.riots, name='riots'),
    url(r'^rally.html$', views.rally, name='rally'),
    url(r'^vip_leader.html$', views.vip_leader, name='vip_leader'),
    url(r'^events_table.html$', views.events_table, name='events_table'),
    url(r'^about.html$', views.about, name='about'),
    url(r'^new_event.html', views.new_event, name='new_event'),

    url(r'^new_event_riots.html', views.new_event_riots, name='new_event_riots'),
    url(r'^new_event_rally.html', views.new_event_rally, name='new_event_rally'),
    url(r'^new_event_vip_leader.html', views.new_event_vip_leader, name='new_event_vip_leader'),
    url(r'^new_event_critical_route.html', views.new_event_critical_route, name='new_event_critical_route'),
]
