from django.shortcuts import render
from .forms import *
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


def index(request):
    return render(request, 'users/index.html')


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
