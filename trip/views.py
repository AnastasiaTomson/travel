from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'trip/index.html')


class ChangeFavouriteTrip(View):
    def post(self, request, **kwargs):
        id = int(request.POST.get('id'))
        trip = Trip.objects.get(id=id)
        favourite = FavouriteTrip.objects.filter(trip=trip)
        if favourite.exists():
            favourite.delete()
        else:
            FavouriteTrip.objects.create(trip=trip, user=request.user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
