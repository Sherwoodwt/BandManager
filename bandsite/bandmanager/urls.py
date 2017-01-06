from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<band_id>[0-9]+)/$', views.band, name='band'),
	url(r'^(?P<band_id>[0-9]+)/tasklist/$', views.tasklist, name='tasklist'),
	url(r'^(?P<band_id>[0-9]+)/tasklist/newtask/$', views.newtask, name='newtask'),
	url(r'^(?P<band_id>[0-9]+)/tasklist/addtask/$', views.addtask, name='addtask'),
]