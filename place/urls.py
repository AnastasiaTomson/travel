from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='place'),
    path('favourite_place/<int:id>', ChangeFavouritePlace.as_view(), name='favourite_place'),
    path('page_pl/<int:id>', page_of_place, name='page_of_place')
]
