from django.shortcuts import render
from trip.models import *
from place.models import *


def front(request):
    places = Place.objects.filter(image__isnull=False).order_by("?")[:8]
    trips = Trip.objects.all().order_by("?")[:3]
    images = Image.objects.all().order_by("?")[:8]
    return render(request, 'front/index.html', locals())