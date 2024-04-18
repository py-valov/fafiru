from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics
from django.db.models import Sum, Count

from .forms import *
from payment.forms import *
from .models import *
from product.models import Products, ProductToTransport
from .serializers import *
from payment.models import Check
from transports.models import Transports

@login_required
def MainPage(request):
    if request.method == 'POST':
        if request.POST['typeForm'] == 'newClient':
            formClientMethod = AddClientForm(request.POST)
            formNewsMethod = AddNewsForm()
            if formClientMethod.is_valid():
                formClientMethod.save()
                return redirect('home')
            
        
        if request.POST['typeForm'] == 'newNews':
            formNewsMethod = AddNewsForm(request.POST)
            formClientMethod = AddClientForm()
            if formNewsMethod.is_valid():
                formNewsMethod.save()
                return redirect('home')
    
    else:
        formClientMethod = AddClientForm()
        formNewsMethod = AddNewsForm()

    formClient = formClientMethod
    formNews = formNewsMethod

    context = {
        'title': "Главная | Fafiru", 
        'formClient': formClient, 
        'formNews': formNews,
    }
    return render(request, 'main/main.html', context)

@login_required
def ClientPage(request, client_id):
    if request.method == 'POST':
        if request.POST['typeForm'] == 'newAppeal':
          formAppealMethod = AddAppealForm(request.POST, request.FILES)
          checkForm = AddChecksForm()
          checkFile = AddFileForm()
          if formAppealMethod.is_valid():
              formAppealMethod.save()
              return redirect('client', client_id)
    
    else:
        formAppealMethod = AddAppealForm()
        checkForm = AddChecksForm()
        checkFile = AddFileForm()
    
    if request.method == 'POST':
        if request.POST['typeForm'] == 'newCheck':
          checkForm = AddChecksForm(request.POST)
          formAppealMethod = AddAppealForm()

          

          if checkForm.is_valid():
              checkForm.save()
              idCheck = checkForm.save().id
              check_id = Check.objects.get(pk=idCheck)

              if request.FILES:
                checkFile = AddFileForm(request.POST, request.FILES)
                files = request.FILES.getlist('PathFile')
                if checkFile.is_valid():
                    for fl in files:
                        flItem = CheckFiles(check_id = check_id, PathFile = fl)
                        flItem.save()
              else:
                checkFile = AddFileForm()

              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          else:
              print('Не получилось')
        
    else: 
        checkForm = AddChecksForm()
        formAppealMethod = AddAppealForm()
        checkFile = AddFileForm()
    
    client = Clients.objects.filter(pk = client_id)
    appeal = Appeal.objects.filter(client = client_id).order_by('-date')
    check = Check.objects.filter(client = client_id).order_by('-date')
    NewIdCheck = Check.objects.count() + 1
    pakings = Products.objects.filter(client_id=client_id)
    transports = ProductToTransport.objects.filter(product_id__client_id=client_id).annotate(Count('transport_id')).order_by('-transport_id__date_create')

    print(transports.values())

    totalPriceInUSD = 0
    totalDeliveryInUSD = 0
    for ch in check:
        if ch.ContractNumber == 'YY2018-30':
          priceInUSD = Operation.objects.filter(check_id=ch.pk)
          for pr in priceInUSD:
              if pr.name == 'Оплата':
                  totalPriceInUSD += pr.priceInUSD
              if pr.name == 'Возврат':
                  totalPriceInUSD -= pr.ReturnPriceUSD
              if pr.name == 'Провоз':
                  totalDeliveryInUSD += pr.productPriceInUSD
    BalanceInUSD = totalPriceInUSD - totalDeliveryInUSD

    context = {
        'title': f'{ client[0].kod } | Fafiru', 
        'p': client[0], 
        'formAppeal': formAppealMethod,
        'appeal': appeal,
        'checkForm': checkForm,
        'check': check,
        'checkFile': checkFile,
        'NewIdCheck': NewIdCheck,
        'totalPriceInUSD': totalPriceInUSD,
        'totalDeliveryInUSD': totalDeliveryInUSD,
        'BalanceInUSD': BalanceInUSD,
        'pakings': pakings,
        'transports': transports,
    }
    return render(request, 'main/client-page.html', context)

@login_required
def AppealItem(request, appeal_id):
    appealItem = Appeal.objects.get(pk = appeal_id)
    if request.method == 'POST':
        if request.POST['type'] == 'AppealUpdate':
          formAppealItem = AddAppealItemForm(instance=appealItem, data=request.POST, files=request.FILES)
          formComments = AppealCommentsForm()
          if formAppealItem.is_valid():
              formAppealItem.save()
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if request.POST['type'] == 'AppealComment':
            formComments = AppealCommentsForm(data=request.POST, files=request.FILES)
            formAppealItem = AddAppealItemForm(instance=appealItem)
            print(formComments.data)
            if formComments.is_valid():
                formComments.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        formAppealItem = AddAppealItemForm(instance=appealItem)
        formComments = AppealCommentsForm()


    # Добавление обратной кнопки на счет
    if appealItem.category == "Счета":
      appealCheck = Check.objects.get(appeal_id = appeal_id)

    if appealItem.category == "Склад":
      appealProduct = Products.objects.get(appeal_id = appeal_id)
      

    appealComments = AppealComments.objects.filter(appeal_id = appeal_id)
    context = {
        'title': f'{ appealItem.category} | Fafiru',
        'appeal': appealItem,
        'formAppeal': formAppealItem,
        'appealItem': appealItem,
        'formComments': formComments,
        'appealComments': appealComments,
    }
    # Добавление обратной кнопки на счет
    if appealItem.category == "Счета":
      context['appealCheck'] = appealCheck
    if appealItem.category == "Склад":
      context['appealProduct'] = appealProduct

    return render(request, 'main/appeal.html', context)

@login_required
def AppealPage(request):
    appeal = Appeal.objects.filter(doneAppeal = False).order_by("-date")
    appealCount = {}
    for ap in appeal:
        if appealCount.get(ap.client.kod, False):
            appealCount[ap.client.kod]['val'] += 1
        else:
            appealCount[ap.client.kod] = {
                'id': ap.client.pk,
                'val': 1,
                'name': ap.client.name
            }
    context = {
        'title': 'Задачи | Fafiru',
        'appeal': appeal,
        'appealCount': appealCount,
    }

    return render(request, 'main/appeal-page.html', context)

@login_required
def AComments(request):
    comments = AppealComments.objects.all().order_by('-pk')[:50]
    appealCount = {}
    appeal = Appeal.objects.filter(doneAppeal = False).order_by("-date")
    for ap in appeal:
        if appealCount.get(ap.client.kod, False):
            appealCount[ap.client.kod]['val'] += 1
        else:
            appealCount[ap.client.kod] = {
                'id': ap.client.pk,
                'val': 1,
                'name': ap.client.name
            }

    context = {
        'title': 'Комментарии | Fafiru',
        'appealCount': appealCount,
        'comments': comments,
        'appeal': appeal,
    }

    return render(request, 'main/appeal-comments.html', context)


class ClientsAPIList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class ClientsAPIUpdate(generics.UpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

