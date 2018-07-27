from django.conf.urls import patterns, include, url
from . import views

app_name = 'ratings'

urlpatterns = [
    url(r'^$', views.ratings_search, name='ratings_search'),
    url(r'^compare', views.ratings_compare, name='ratings_compare'),
    url(r'^reporting', views.ratings_reporting, name='ratings_reporting'),
    url(r'^add_module', views.ratings_add_module, name='ratings_add_module'),
    url(r'^insert_data', views.insert_data, name='insert_data'),
    url(r'^upload_xml', views.upload_xml, name='upload_xml'),
    url(r'^upload_csv', views.upload_csv, name='upload_csv'),
]