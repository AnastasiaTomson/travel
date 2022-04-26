from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'place/index.html')


class ChangeFavouritePlace(View):
    def get(self, request, id):
        place = Place.objects.get(id=id)
        favourite = FavouritePlace.objects.filter(place=place)
        if favourite.exists():
            favourite.delete()
        else:
            FavouritePlace.objects.create(place=place, user=request.user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
