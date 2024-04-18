"""fafiru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from fafiru import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main.views import *
from payment.views import ChecksAPIList, OperationsAPIList, ChecksNoPaymentAPIList
from product.views import ProductAPIList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/clientlist/', ClientsAPIList.as_view()),
    path('api/v1/clientlist/<int:pk>/', ClientsAPIUpdate.as_view()),
    path('api/v1/newslist/', NewsAPIList.as_view()),
    path('api/v1/checkslist/', ChecksAPIList.as_view()),
    path('api/v1/nopaymentlist/', ChecksNoPaymentAPIList.as_view()),
    path('api/v1/operationslist/', OperationsAPIList.as_view()),
    path('api/v1/productslist/', ProductAPIList.as_view()),
    path('', include('main.urls')),
    path('finance/', include('payment.urls')),
    path('product/', include('product.urls')),
    path('auth/', include('users.urls')),
    path('transports/', include('transports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)