from django.shortcuts import render
from .forms import *
from .serializers import *
from trip.form import *
from place.models import *
from trip.models import *
from .admin import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics
import json
from django.core.cache import cache
from django.template.loader import render_to_string


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse('front'))


@login_required()
def logout_user(request):
    """
    Выход пользователя из системы
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse('front'))


@login_required()
def index(request):
    title = 'Главная'
    top_places = Place.objects.all()[:3]
    top_trips = Trip.objects.all()[:3]
    return render(request, 'users/index.html', locals())


@login_required()
def favourite(request):
    title = 'Избранное'
    trips = FavouriteTrip.objects.all()
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='users/place_list_like.html',
                    context={
                        'places': get_paginated_page(request, FavouritePlace.objects.all(), 5)}
                )
            })
    return render(request=request, template_name='users/favourite.html',
                  context={'places': get_paginated_page(request, FavouritePlace.objects.all(), 5),
                           'trips': trips, 'title': title})


@login_required()
def user_trips(request):
    title = 'Мои туры'
    trips = UserTrip.objects.all()
    trips_paginator = Paginator(trips, 6)
    trips_page_number = request.GET.get('page_trip', 1)
    trips_page_obj = trips_paginator.get_page(trips_page_number)
    if trips.exists():
        return render(request, 'users/my_trips.html', locals())
    else:
        return HttpResponseRedirect(reverse('create_user_trip'))


@login_required()
def my_trip(request, id):
    trip = UserTrip.objects.get(id=id)
    title = trip.title
    places = UserPlace.objects.filter(trip=trip).order_by('visit_date', 'visit_time')
    return render(request, 'users/my_trip.html', locals())


@login_required()
def edit_my_trip(request, id):
    trip = UserTrip.objects.get(id=id)
    title = trip.title
    user_trip_form = UserTripForm(request.POST if request.POST else None, request_user=request.user, instance=trip)
    if request.method == 'POST':
        if user_trip_form.is_valid():
            user_trip_form.save()
            return HttpResponseRedirect(reverse('my_trip', args={id: id}))
    return render(request, 'users/edit_my_trip.html', locals())


@login_required()
def delete_user_trip(request, id):
    trip = UserTrip.objects.get(id=id)
    trip.delete()
    return HttpResponseRedirect(reverse('user_trips'))


@login_required()
def edit_my_trip_places(request, id):
    trip = UserTrip.objects.get(id=id)
    title = trip.title
    places = Place.objects.exclude(id__in=trip.place_in_trip())
    place_paginator = Paginator(places, 6)
    place_page_number = request.GET.get('page_place', 1)
    place_page_obj = place_paginator.get_page(place_page_number)
    formset = ChildrenFormset(request.POST if request.POST else None, instance=trip)
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            try:
                del request.session['id_places']
            except KeyError:
                pass
            return HttpResponseRedirect(reverse('my_trip', args={id: id}))
    return render(request, 'users/edit_my_trip_places.html', locals())


def get_paginated_page(request, objects, number=10):
    current_page = Paginator(objects, number)
    page = request.GET.get('page') if request.method == 'GET' else request.POST.get('page')
    try:
        return current_page.page(page)
    except PageNotAnInteger:
        return current_page.page(1)
    except EmptyPage:
        return current_page.page(current_page.num_pages)


@login_required()
def add_my_trip_place(request, id):
    trip = UserTrip.objects.get(id=id)
    title = trip.title
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='users/place.html',
                    context={
                        'places': get_paginated_page(request, Place.objects.exclude(id__in=trip.place_in_trip()), 5)}
                )
            })
        else:
            for i in request.POST.getlist('place'):
                place = Place.objects.get(id=int(i))
                UserPlace.objects.create(place=place, trip=trip)
            return HttpResponseRedirect(reverse('my_trip', args={id: id}))
    return render(request=request, template_name='users/add_my_trip_places.html',
                  context={'places': get_paginated_page(request, Place.objects.exclude(id__in=trip.place_in_trip()), 5),
                           'id': id, 'title': title})

from django.forms.models import model_to_dict
@login_required()
def set_formset_user_trip(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            ChildrenFormset1 = inlineformset_factory(UserTrip, UserPlace, fields='__all__', can_delete=True,
                                                     extra=len(request.session['id_places']),
                                                     widgets={
                                                         'visit_date': forms.DateInput(attrs={'class': 'date'},
                                                                                       format='%d.%m.%Y'),
                                                         'visit_time': forms.TimeInput(attrs={'type': 'time', 'class': 'time'},
                                                                                       format='%H:%M'),
                                                         'place': forms.NumberInput(),
                                                     })
            pl_session = Place.objects.filter(id__in=request.session['id_places'])
            formset = ChildrenFormset1()
            for i, p in enumerate(pl_session):
                formset.forms[i].initial['place'] = p
            return JsonResponse({
                "result": True,
                "articles": render_to_string(
                    request=request,
                    template_name='users/places_with_date.html',
                    context={'formset': formset}
                )
            })


@login_required()
def create_user_trip(request):
    title = 'Создать тур'
    user_trip_form = UserTripForm(request.POST if request.POST else None, request_user=request.user)
    if request.method == 'POST':
        if user_trip_form.is_valid():
            user_trip_object = user_trip_form.save()
            formset = ChildrenFormset(request.POST, instance=user_trip_object)
            if formset.is_valid():
                formset.save()
                del request.session['id_places']
                return HttpResponse(
                    json.dumps({'status': True}),
                    content_type="application/json"
                )
        return HttpResponse(
            json.dumps({'status': False}),
            content_type="application/json"
        )
    else:
        places = Place.objects.all()
        place_paginator = Paginator(places, 5)
        place_page_number = request.GET.get('page_place', 1)
        place_page_obj = place_paginator.get_page(place_page_number)
        return render(request=request, template_name='users/create_user_trip.html',
                      context={'user_trip_form': user_trip_form, 'place_page_obj': place_page_obj,
                               'title': title})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('front'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', locals())


@login_required()
def edit_profile(request):
    user = MyUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('front'))
    else:
        form = UserCreationForm(instance=user)
    return render(request, 'users/user.html', locals())


def set_cache(request):
    id = request.GET.get('id')
    list_id_places = request.session.get('id_places')
    if list_id_places is None:
        list_id_places = []
    if int(id) not in list_id_places:
        list_id_places.append(int(id))
    else:
        list_id_places.remove(int(id))
    request.session['id_places'] = list_id_places
    return HttpResponse(
        json.dumps({'status': True}),
        content_type="application/json"
    )


class PlaceGet(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        places = Place.objects.filter(id__in=self.request.session['id_places'])
        return places
