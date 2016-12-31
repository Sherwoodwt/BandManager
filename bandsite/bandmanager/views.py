from django.shortcuts import render
from django.http import HttpResponse

from .models import Band

# Create your views here.
def index(request):
	return HttpResponse("This is a Homepage test")

def band(request, band_id):
	cur = Band.objects.get(id=band_id)
	return HttpResponse("Bandpage. Band: %s" % cur)
