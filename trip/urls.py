from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='trip'),
    path('favourite_trip/<int:id>', ChangeFavouriteTrip.as_view(), name='favourite_trip'),
    path('page_tr/<int:id>', page_of_trip, name='page_of_trip')
]
