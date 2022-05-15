from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='place'),
    path('favourite_place/<int:id>', ChangeFavouritePlace.as_view(), name='favourite_place')
]
