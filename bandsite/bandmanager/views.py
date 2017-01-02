from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Band

# Create your views here.
def index(request):
	return render(request, "index.html")

def band(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	members = band.member_set.all()
	context = {"band": band, "members": members}
	return render(request, "band.html", context)

def tasklist(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	tasks = band.task_set.all()
	context = {"band": band, "tasks": tasks}
	return render(request, "tasklist.html", context)