from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from ..models import Band, Task, Member, TaskComment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    	return HttpResponseRedirect(reverse('band'))


@login_required(login_url='/login/')
def band(request):
	user = request.user
	band = get_object_or_404(Band, pk=user.member.band.id)
	members = band.member_set.filter(active=1)
	context = {"band": band, "members": members}
	return render(request, "band.html", context)


@login_required(login_url='/login')
def createmember(request):
	return HttpResponse("made it bois")