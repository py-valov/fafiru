from django.urls import path
from .views import *

urlpatterns = [
    path('', Product, name='product'),
    path('new/', ProductNew, name='productNew'),
    path('old/', ProductOld, name='productOld'),
    path('item/<int:product_id>/', ProductPage, name='item'),
    path('page/<int:page_number>/', Product, name='paginator'),
]
