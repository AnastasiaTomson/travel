from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import *
from django.views import View
from trip.models import *
from trip.form import UserTripForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def index(request):
    title = 'Каталог мест'
    places = Place.objects.all().order_by("?")[:12]
    # if request.method == 'POST':
    #     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #         return JsonResponse({
    #             "result": True,
    #             "articles": render_to_string(
    #                 request=request,
    #                 template_name='place/index.html',
    #                 context={
    #                     'places': get_paginated_page(request, Place.objects.all(), 12)}
    #             )
    #         })
    # return render(request=request, template_name='place/index.html',
    #               context={'places': get_paginated_page(request, Place.objects.all(), 12),
    #                         'title': title})
    return render(request, 'place/index.html', locals())


def page_of_place(request, id):
    # title = 'Страница места'
    place = Place.objects.get(id=id)
    title = place.title
    return render(request, 'place/page_of_place.html', locals())


def get_paginated_page(request, objects, number=10):
    current_page = Paginator(objects, number)
    page = request.GET.get('page') if request.method == 'GET' else request.POST.get('page')
    try:
        return current_page.page(page)
    except PageNotAnInteger:
        return current_page.page(1)
    except EmptyPage:
        return current_page.page(current_page.num_pages)


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
