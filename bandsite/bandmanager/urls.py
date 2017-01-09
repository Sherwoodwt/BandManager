from django.conf.urls import url



from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^band/$', views.band, name='band'),
	url(r'^tasklist/$', views.tasklist, name='tasklist'),
	url(r'^newtask/$', views.newtask, name='newtask'),
	url(r'^addtask/$', views.addtask, name='addtask'),
	url(r'^task/(?P<task_id>[0-9]+)/', views.task, name='task'),
]