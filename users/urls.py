from django.urls import path
from .views import *

urlpatterns = [
    path('authorization/', Authorization, name ='authorization'),
    path('registration/', Registration, name ='registration'),
    path('logout/', logout, name ='logout'),
]