from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage, name ='home'),
    path('client-page/<int:client_id>/', ClientPage, name='client'),
    path('appeal/<int:appeal_id>/', AppealItem, name='appeal'),
    path('appeal-page/', AppealPage, name='appealPage'),
    path('appeal-comments/', AComments, name='appealComments'),
]
