from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from product.models import ProductToTransport
from django.db.models import Sum

@login_required
def Transport(request):

    if request.method == 'POST':
        if request.POST['type'] == 'CreateTransport':
            createTransport = CreateTransport(request.POST)
            if createTransport.is_valid():
                createTransport.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        createTransport = CreateTransport()
    
    transportLoading = Transports.objects.filter(status='Сбор на складе').order_by('-date_create')
    transportSVH = Transports.objects.filter(status='СВХ').order_by('-date_create')
    transportCustoms = Transports.objects.filter(status='Таможня').order_by('-date_create')
    transportUnloading = Transports.objects.filter(status='Выпуск/разгрузка').order_by('-date_create')
    transportProductReporting = Transports.objects.filter(status='Отчетность на товар').order_by('-date_create')
    transportClose = Transports.objects.filter(status='Закрыта').order_by('-date_create')

    context = {
        'title': 'Провозы | Fafiru',
        'transportLoading': transportLoading,
        'transportSVH': transportSVH,
        'transportCustoms': transportCustoms,
        'transportUnloading': transportUnloading,
        'transportProductReporting': transportProductReporting,
        'transportClose': transportClose,
    }

    return render(request, 'transport/transport.html', context )