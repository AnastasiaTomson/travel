from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='user'),
    path('register/', register_user, name='register'),
    path('login_user/', login_user, name='login_user'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout_user/', logout_user, name='logout_user')
]