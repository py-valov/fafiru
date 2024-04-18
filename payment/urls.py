from django.urls import path

from .views import *

urlpatterns = [
    path('', Finance, name ='finance'),
    path('payment/<int:payment_id>/', Payment, name ='payment'),
    path('balance/', Balance, name ='balance'),
]