from django.urls import path, include
from .views import *

urlpatterns = [
    path('', front, name='front'),
    path('feedback', feedback, name='feedback')
]
