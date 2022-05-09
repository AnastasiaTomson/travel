from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='user'),
    path('favourite/', favourite, name='favourite'),
    path('user_trips/', user_trips, name='user_trips'),
    path('my_trip/<int:id>', my_trip, name='my_trip'),
    path('edit_my_trip/<int:id>', edit_my_trip, name='edit_my_trip'),
    path('edit_my_trip_places/<int:id>', edit_my_trip_places, name='edit_my_trip_places'),
    path('create_user_trip/', create_user_trip, name='create_user_trip'),
    path('place_get/', PlaceGet.as_view(), name="place_get"),
    path('register/', register_user, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout_user/', logout_user, name='logout_user'),
    path('set_cache/', set_cache, name='set_cache')
]