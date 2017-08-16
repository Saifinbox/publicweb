from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^cat/energy/$', views.energy, name='energy'),
    url(r'^cat/transport/$', views.transport, name='transport'),
    url(r'^cat/env/$', views.env, name='env'),
    url(r'^cat/agriculture/$', views.agriculture, name='agriculture'),
    url(r'^energy/data/kelec/$', views.kelec, name='kelec'),
    url(r'^env/data/monum/$', views.monum, name='monum'),
    url(r'^data/upload/$', views.upload, name='upload'),



]
