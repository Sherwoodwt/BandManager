from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

from .models import Band

# Create your views here.
def index(request):
	return render(request, "index.html")

def band(request, band_id):
	band = Band.objects.get(id=band_id)
	members = band.member_set.all()
	context = {"band": band, "members": members}
	return render(request, "band.html", context)
