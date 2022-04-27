from django.shortcuts import render
from .forms import *
from place.models import *
from trip.models import *
from .admin import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password


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


from django.core.paginator import Paginator


@login_required()
def favourite(request):
    title = 'Избранное'
    favourite_places = FavouritePlace.objects.all()
    favourite_trips = FavouriteTrip.objects.all()
    place_paginator = Paginator(favourite_places, 4)  # Покажет 4 избранных места при пагинации
    trip_paginator = Paginator(favourite_trips, 3)  # Покажет 6 избранных туров при пагинации
    place_page_number = request.GET.get('page_place')
    place_page_obj = place_paginator.get_page(place_page_number)
    trip_page_number = request.GET.get('page_trip')
    trip_page_obj = trip_paginator.get_page(trip_page_number)
    return render(request, 'users/favourite.html', locals())


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('front'))
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', locals())


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
