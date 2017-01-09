from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from .models import Band, Task, Member
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):
    	return HttpResponseRedirect(reverse('band'))


@login_required(redirect_field_name='login')
def band(request):
	user = request.user
	band = get_object_or_404(Band, pk=user.member.band.id)
	members = band.member_set.filter(active=1)
	context = {"band": band, "members": members}
	return render(request, "band.html", context)


@login_required(redirect_field_name='login')
def tasklist(request):
	user = request.user
	band = get_object_or_404(Band, pk=user.member.band.id)
	tasks = band.task_set.all()
	context = {"band": band, "tasks": tasks}
	return render(request, "tasklist.html", context)


@login_required(redirect_field_name='login')
def newtask(request):
	user = request.user
	band = get_object_or_404(Band, pk=user.member.band.id)
	members = band.member_set.all()
	context = {"band": band, "members": members}
	return render(request, "newtask.html", context)


#handles adding new tasks from newtask page
@login_required(redirect_field_name='login')
def addtask(request):
	user = request.user
	title = request.POST['TaskTitle']
	description = request.POST['TaskDescription']
	difficulty = request.POST['TaskDifficulty']
	priority = request.POST['TaskPriority']
	member = request.POST['TaskAssignee']
	newTask = Task(band=Band.objects.get(pk=user.member.band.id), title=title, description=description, difficulty=difficulty, priority=priority)

	#attempt to read member, if member is not None, assign that member to the Task
	memberIfThere = None
	try:
		memberIfThere = Member.objects.get(pk=member)
	except:
		memberIfThere = None
	
	if memberIfThere != None:
		newTask.member = memberIfThere

	newTask.save()
	return HttpResponseRedirect(reverse('tasklist'))


@login_required(redirect_field_name='login')
def task(request, task_id):
	user = request.user
	band_id = user.member.band.id
	band = get_object_or_404(Band, pk=band_id)
	task = band.task_set.get(pk=task_id)
	taskComments = task.taskcomment_set.all()
	context = {"band": band, "task": task, "taskComments": taskComments}
	return render(request, "task.html", context)