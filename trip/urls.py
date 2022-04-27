from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('favourite_trip/<int:id>', ChangeFavouriteTrip.as_view(), name='favourite_trip')
]
