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


# after django registration form registers users, member creation form is displayed
def createmember(request):
	user = request.user
	bandList = Band.objects.all()
	context = {"bands": bandList}
	return render(request, "createmember.html", context)

# creates and saves member based on input from createmember
def makeMemberObject(request):
	user = request.user
	selectedBand = request.POST['selectedBand']
	selectedPicture = request.POST['selectedPicture']
	newMember = Member(band=Band.objects.get(pk=selectedBand), user=user, name=user.username, contact_info=user.email, picture_url=selectedPicture)
	newMember.save()
	return reverse('band')