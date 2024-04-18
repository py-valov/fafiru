from django.urls import path
from .views import *

urlpatterns = [
    path('', Transport, name='transport'),
]