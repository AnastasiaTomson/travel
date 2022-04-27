from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def index(request):
    return render(request, 'place/index.html')


class ChangeFavouritePlace(View):
    def get(self, request, id):
        kwargs = {}
        try:
            place = Place.objects.get(id=id)
            favourite = FavouritePlace.objects.filter(place=place)
            if favourite.exists():
                favourite.delete()
                type = 'deactivate'
            else:
                FavouritePlace.objects.create(place=place, user=request.user)
                type = 'active'
            kwargs['type'] = type
            kwargs['status'] = 1
        except Exception:
            kwargs['status'] = 0
        return JsonResponse({**kwargs})
