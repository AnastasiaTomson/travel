from django.shortcuts import render
from trip.models import *


def front(request):
    trips = Trip.objects.all()
    return render(request, 'front/index.html', locals())
