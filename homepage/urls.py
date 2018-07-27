from django.conf.urls import patterns, include, url
from . import views

app_name = 'homepage'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact_us', views.contact_us, name='contact_us'),
    url(r'^about_us', views.about_us, name='about_us'),
    url(r'^our_team', views.our_team, name='our_team'),
]