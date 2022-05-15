from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def index(request):
    trips = Trip.objects.all().order_by("?")[:4]
    # images = Image.objects.all().order_by("?")[:4]
    return render(request, 'trip/index.html', locals())


class ChangeFavouriteTrip(View):
    def get(self, request, id):
        kwargs = {}
        try:
            trip = Trip.objects.get(id=id)
            favourite = FavouriteTrip.objects.filter(trip=trip)
            if favourite.exists():
                favourite.delete()
                type = 'deactivate'
            else:
                FavouriteTrip.objects.create(trip=trip, user=request.user)
                type = 'active'
            kwargs['type'] = type
            kwargs['status'] = 1
        except Exception:
            kwargs['status'] = 0
        return JsonResponse({**kwargs})
