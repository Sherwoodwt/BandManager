from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from .models import Band, Task, Member
from django.contrib.auth.models import User


def index(request):
    	return HttpResponse("good")

def band(request, user_id):
	user = User.objects.get(pk=user_id)
	band = get_object_or_404(Band, pk=user.member.band)
	members = band.member_set.filter(active=1)
	context = {"band": band, "members": members}
	return render(request, "band.html", context)


def tasklist(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	tasks = band.task_set.all()
	context = {"band": band, "tasks": tasks}
	return render(request, "tasklist.html", context)


def newtask(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	members = band.member_set.all()
	context = {"band": band, "members": members}
	return render(request, "newtask.html", context)


#handles adding new tasks from newtask page
def addtask(request, band_id):
	title = request.POST['TaskTitle']
	description = request.POST['TaskDescription']
	difficulty = request.POST['TaskDifficulty']
	priority = request.POST['TaskPriority']
	member = request.POST['TaskAssignee']
	newTask = Task(band=Band.objects.get(pk=band_id), member=Member.objects.get(pk=member), title=title, description=description, difficulty=difficulty, priority=priority)
	newTask.save()
	return HttpResponseRedirect(reverse('tasklist', args=band_id))


def task(request, band_id, task_id):
	band = get_object_or_404(Band, pk=band_id)
	task = get_object_or_404(Task, pk=task_id)
	taskComments = task.taskcomment_set.all()
	context = {"band": band, "task": task, "taskComments": taskComments}
	return render(request, "task.html", context)