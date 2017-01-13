from django.conf.urls import url



from views import views, taskviews

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^band/$', views.band, name='band'),
	url(r'^tasklist/$', taskviews.tasklist, name='tasklist'),
	url(r'^tasklist/filter/$', taskviews.filterTasklist, name='filterTasklist'),
	url(r'^newtask/$', taskviews.newtask, name='newtask'),
	url(r'^addtask/$', taskviews.addtask, name='addtask'),
	url(r'^task/(?P<task_id>[0-9]+)/$', taskviews.task, name='task'),
	url(r'^assigntask/(?P<task_id>[0-9]+)/$', taskviews.assignTask, name='assignTask'),
	url(r'^completeTask/(?P<task_id>[0-9]+)/$', taskviews.completeTask, name='completeTask'),
	url(r'^unassignTask/(?P<task_id>[0-9]+)/$', taskviews.unassignTask, name='unassignTask'),
	url(r'^deleteTask/(?P<task_id>[0-9]+)/$', taskviews.deleteTask, name='deleteTask'),
	url(r'^makeComment/(?P<task_id>[0-9]+)/$', taskviews.makeComment, name='makeComment'),
	url(r'^task/(?P<task_id>[0-9]+)/deleteComment/(?P<comment_id>[0-9]+)/$', taskviews.deleteComment, name='deleteComment')
]