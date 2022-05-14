from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='user'),
    path('favourite/', favourite, name='favourite'),
    path('user_trips/', user_trips, name='user_trips'),
    path('my_trip/<int:id>', my_trip, name='my_trip'),
    path('edit_my_trip/<int:id>', edit_my_trip, name='edit_my_trip'),
    path('delete_user_trip/<int:id>', delete_user_trip, name='delete_user_trip'),
    path('edit_my_trip_places/<int:id>', edit_my_trip_places, name='edit_my_trip_places'),
    path('add_my_trip_place/<int:id>', add_my_trip_place, name='add_my_trip_place'),
    path('create_user_trip/', create_user_trip, name='create_user_trip'),
    path('set_formset_user_trip/', set_formset_user_trip, name='set_formset_user_trip'),
    path('place_get/', PlaceGet.as_view(), name="place_get"),
    path('register/', register_user, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('user_profile/', user_profile, name='user_profile'),
    path('edit_user_profile/', edit_user_profile, name='edit_user_profile'),
    path('edit_password_user_profile/', edit_password_user_profile, name='edit_password_user_profile'),
    path('logout_user/', logout_user, name='logout_user'),
    path('set_cache/', set_cache, name='set_cache')
]