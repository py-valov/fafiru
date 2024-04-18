from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from datetime import date

from .forms import *
from transports.forms import CreateTransport
from payment.forms import AddOperationsToTransport
from main.forms import AddAppealForm
from main.models import Clients
from transports.models import Transports
from payment.models import Check, Operation
from .models import *
from .serializers import *

@login_required
def Product(request, page_number=1):
    
    if request.method == 'POST':
        if request.POST['type'] == 'newProduct':
          newProduct = AddProducts(request.POST)
          if newProduct.is_valid():
              newProduct.save()
              p_id = newProduct.save().id
              weight = newProduct.save().weight
              volume = newProduct.save().volume
              price = newProduct.save().price

              weightBalance = Products.objects.filter(pk = p_id).update(weightBalance = weight)
              volumeBalance = Products.objects.filter(pk = p_id).update(volumeBalance = volume)
              priceBalance = Products.objects.filter(pk = p_id).update(priceBalance = price)
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif request.POST['type'] == 'Код клиента':
            client = Clients.objects.filter(kod__icontains = request.POST['filter'])
            if client:
              for c in client :
                  products = Products.objects.filter(client_id = c.id)
                  productsAll = products.exclude(status = 'Отгружен').order_by('-date')  
              newProduct = AddProducts()
            else:
               productsAll = Products.objects.filter(status = 'нет').order_by('-date')
               newProduct = AddProducts()
        
        elif request.POST['type'] == 'Товар':
            products = Products.objects.filter(nameProduct__icontains = request.POST['filter'])  
            productsAll = products.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Имя пакинга':
            products = Products.objects.filter(namePaking__icontains = request.POST['filter'])
            productsAll = products.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Транспорт':
            products = Products.objects.filter(transport__icontains = request.POST['filterTransport'])
            productsAll = products.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'cleare':
           productsAll = Products.objects.exclude(status = 'Отгружен').order_by('-date')
           newProduct = AddProducts()
    else:
      newProduct = AddProducts()
      productsAll = Products.objects.exclude(status = 'Отгружен').order_by('-date')
    
    paginator = Paginator(productsAll, 12)
    products_paginator = paginator.page(page_number)
    clients = Clients.objects.all()
    
    context = {
        'title': 'На складе | Fafiru',
        'newProduct': newProduct,
        'clients': clients,
        'productsAll': products_paginator,
    }
    return render(request, 'product/product.html', context)

@login_required
def ProductNew(request, page_number=1):
    current_date = datetime.today().date() - timedelta(days=2)
    if request.method == 'POST':
        if request.POST['type'] == 'newProduct':
          newProduct = AddProducts(request.POST)
          if newProduct.is_valid():
              newProduct.save()
              p_id = newProduct.save().id
              weight = newProduct.save().weight
              volume = newProduct.save().volume
              price = newProduct.save().price

              weightBalance = Products.objects.filter(pk = p_id).update(weightBalance = weight)
              volumeBalance = Products.objects.filter(pk = p_id).update(volumeBalance = volume)
              priceBalance = Products.objects.filter(pk = p_id).update(priceBalance = price)
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif request.POST['type'] == 'Код клиента':
            client = Clients.objects.filter(kod__icontains = request.POST['filter'])
            if client:
              for c in client :
                  products = Products.objects.filter(client_id = c.id)
                  productDate = products.filter(date__gte = current_date)
                  productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')  
              newProduct = AddProducts()
            else:
               productsAll = Products.objects.filter(status = 'нет').order_by('-date')
               newProduct = AddProducts()
        
        elif request.POST['type'] == 'Товар':
            products = Products.objects.filter(nameProduct__icontains = request.POST['filter'])
            productDate = products.filter(date__gte = current_date)  
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Имя пакинга':
            products = Products.objects.filter(namePaking__icontains = request.POST['filter'])
            productDate = products.filter(date__gte = current_date)
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Транспорт':
            products = Products.objects.filter(transport__icontains = request.POST['filterTransport'])
            productDate = products.filter(date__gte = current_date)
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'cleare':
           products = Products.objects.filter(date__gte = current_date)
           productsAll = products.exclude(status = 'Отгружен').order_by('-date')
           newProduct = AddProducts()
    else:
      newProduct = AddProducts()
      products = Products.objects.filter(date__gte = current_date)
      productsAll = products.exclude(status = 'Отгружен').order_by('-date')
    
    paginator = Paginator(productsAll, 12)
    products_paginator = paginator.page(page_number)
    clients = Clients.objects.all()
    
    context = {
        'title': 'Новые | Fafiru',
        'newProduct': newProduct,
        'clients': clients,
        'productsAll': products_paginator,
    }
    return render(request, 'product/product-new.html', context)

@login_required
def ProductOld(request, page_number=1):
    current_date = datetime.today().date() - timedelta(days=7)

    if request.method == 'POST':
        if request.POST['type'] == 'newProduct':
          newProduct = AddProducts(request.POST)
          if newProduct.is_valid():
              newProduct.save()
              p_id = newProduct.save().id
              weight = newProduct.save().weight
              volume = newProduct.save().volume
              price = newProduct.save().price

              weightBalance = Products.objects.filter(pk = p_id).update(weightBalance = weight)
              volumeBalance = Products.objects.filter(pk = p_id).update(volumeBalance = volume)
              priceBalance = Products.objects.filter(pk = p_id).update(priceBalance = price)
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        elif request.POST['type'] == 'Код клиента':
            client = Clients.objects.filter(kod__icontains = request.POST['filter'])
            if client:
              for c in client :
                  products = Products.objects.filter(client_id = c.id)
                  productDate = products.filter(date__lte = current_date)
                  productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')  
              newProduct = AddProducts()
            else:
               productsAll = Products.objects.filter(status = 'нет').order_by('-date')
               newProduct = AddProducts()
        
        elif request.POST['type'] == 'Товар':
            products = Products.objects.filter(nameProduct__icontains = request.POST['filter'])
            productDate = products.filter(date__lte = current_date)
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Имя пакинга':
            products = Products.objects.filter(namePaking__icontains = request.POST['filter'])
            productDate = products.filter(date__lte = current_date)
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'Транспорт':
            products = Products.objects.filter(transport__icontains = request.POST['filterTransport'])
            productDate = products.filter(date__lte = current_date)
            productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
            newProduct = AddProducts()

        elif request.POST['type'] == 'cleare':
           productDate = Products.objects.filter(date__lte = current_date)
           productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
           newProduct = AddProducts()
    else:
      newProduct = AddProducts()
      productDate = Products.objects.filter(date__lte = current_date)
      productsAll = productDate.exclude(status = 'Отгружен').order_by('-date')
    
    paginator = Paginator(productsAll, 12)
    products_paginator = paginator.page(page_number)
    clients = Clients.objects.all()
    
    context = {
        'title': 'Долголежки | Fafiru',
        'newProduct': newProduct,
        'clients': clients,
        'productsAll': products_paginator,
    }
    return render(request, 'product/product-old.html', context)

@login_required
def ProductPage(request, product_id):
    comment = Comments.objects.filter(product_id = product_id)
    productItem = Products.objects.get(pk = product_id)
    if request.method == "POST":
       if request.POST['type'] == "newComment":
          if comment:
            for c in comment:
              commentForm = AddComment(request.POST, instance=c)
          else:
            commentForm = AddComment(request.POST)
          updateProduct = UpdateProduct(instance = productItem)
          productFile = AddFileProduct()
          createTransport = CreateTransport()
          AddOperations = AddOperationsToTransport()
          AddProductToTransport = AddProductToTransportForm()

          if commentForm.is_valid():
             commentForm.save()
             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      
       elif request.POST['type'] == "updateProduct":
          weightOld = Products.objects.get(pk=product_id).weight
          volumeOld = Products.objects.get(pk=product_id).volume
          priceOld = Products.objects.get(pk=product_id).price
          contract = Products.objects.get(pk=product_id).ContractNumber

          updateProduct = UpdateProduct(request.POST, instance = productItem)
          if comment:
            for c in comment:
              commentForm = AddComment(instance=c)
          else:
            commentForm = AddComment()
          if updateProduct.is_valid():
             updateProduct.save()
             itemId = updateProduct.save().id
             weight = updateProduct.save().weight
             volume = updateProduct.save().volume
             price = updateProduct.save().price

             weightBalance = updateProduct.save().weightBalance
             volumeBalance = updateProduct.save().volumeBalance
             priceBalance = updateProduct.save().priceBalance

             weightBalanceNew = weightBalance + (weight - weightOld)
             volumeBalanceNew = volumeBalance + (volume - volumeOld)
             priceBalanceNew = priceBalance + (price - priceOld)

             Products.objects.filter(pk=itemId).update(weightBalance=weightBalanceNew)
             Products.objects.filter(pk=itemId).update(volumeBalance=volumeBalanceNew)
             Products.objects.filter(pk=itemId).update(priceBalance=priceBalanceNew)
             Products.objects.filter(pk=itemId).update(ContractNumber=contract)

             if request.FILES:
                productFile = AddFileProduct(request.POST, request.FILES)
                files = request.FILES.getlist('file')
                if productFile.is_valid():
                    for fl in files:
                        flItem = ProductFiles(product_id = productItem, file = fl)
                        flItem.save()
             else:
                productFile = AddFileProduct()
                createTransport = CreateTransport()
                AddOperations = AddOperationsToTransport()
                AddProductToTransport = AddProductToTransportForm()

             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          
       elif request.POST['type'] == "ProductToTransport":
          if comment:
            for c in comment:
              commentForm = AddComment(instance=c)
          else:
            commentForm = AddComment()
          AddOperations = AddOperationsToTransport(request.POST)
          AddProductToTransport = AddProductToTransportForm(request.POST)
          productFile = AddFileProduct()
          createTransport = CreateTransport()

          if AddProductToTransport.is_valid():
             AddProductToTransport.save()
             AddProductToTransport_id = AddProductToTransport.save().id
             if AddOperations.is_valid():
                AddOperations.save()
                AddOperations_id = AddOperations.save().id
                if productItem.ContractNumber == "YY2018-30":
                  summ = AddOperations.save().productPriceInUSD
                  Clients.objects.filter(pk=productItem.client_id.pk).update(negativeBalance=summ)

                productPaking = Products.objects.filter(pk=product_id)
                deliveryWeight = AddProductToTransport.save().weight
                deliveryVolume = AddProductToTransport.save().volume
                deliveryPrice = AddOperations.save().productPriceInUSD

                weightPaking = 0
                volumePaking = 0
                pricePaking = 0
                for item in productPaking:
                   weightPaking += item.weightBalance
                   volumePaking += item.volumeBalance
                   pricePaking += item.priceBalance

                balanceWeightPaking = weightPaking - deliveryWeight
                balanceVolumePaking = volumePaking - deliveryVolume
                balancePricePaking = pricePaking - deliveryPrice

                Operation.objects.filter(pk=AddOperations_id).update(productToTransport_id=AddProductToTransport_id)
                Products.objects.filter(pk=product_id).update(weightBalance=balanceWeightPaking)
                Products.objects.filter(pk=product_id).update(volumeBalance=balanceVolumePaking)
                Products.objects.filter(pk=product_id).update(priceBalance=balancePricePaking)

                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       elif request.POST['type'] == 'newAppealProduct':
          if comment:
            for c in comment:
              commentForm = AddComment(instance=c)
          else:
            commentForm = AddComment()
          AddOperations = AddOperationsToTransport()
          AddProductToTransport = AddProductToTransportForm()
          productFile = AddFileProduct()
          createTransport = CreateTransport()

          AddAppealProduct = AddAppealForm(request.POST)
          if AddAppealProduct.is_valid():
             AddAppealProduct.save()
             AddAppealProduct_id = AddAppealProduct.save().id
             Products.objects.filter(pk=product_id).update(appeal=AddAppealProduct_id)

             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

       elif request.POST['type'] == 'DeleteFile':
          if comment:
            for c in comment:
              commentForm = AddComment(instance=c)
          else:
            commentForm = AddComment()
          updateProduct = UpdateProduct(instance = productItem)
          productFile = AddFileProduct()
          fileItem = ProductFiles.objects.get(id=request.POST['file_id'])
          fileItem.file.delete(save=True)
          fileItem.delete()
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
      if comment:
        for c in comment:
          commentForm = AddComment(instance=c)
      else:
        commentForm = AddComment()
      productFile = AddFileProduct()
      updateProduct = UpdateProduct(instance = productItem)
      createTransport = CreateTransport()
      AddOperations = AddOperationsToTransport()
      AddProductToTransport = AddProductToTransportForm()
    
    
    fileItems = ProductFiles.objects.filter(product_id = product_id)
    clients = Clients.objects.all()
    priceClient = Check.objects.filter(client_id = productItem.client_id.pk)
    transport = Transports.objects.exclude(status = 'Закрыта').order_by("-date_create")
    operation = Operation.objects.filter(productToTransport_id__product_id=product_id)
    today = date.today()

    
    context = {
        'title': f'{productItem.namePaking} | Fafiru',
        'productItem': productItem,
        'fileItems': fileItems,
        'commentForm': commentForm,
        'updateProduct': updateProduct,
        'clients': clients,
        'productFile': productFile,
        'priceClient': priceClient,
        'transport': transport,
        'createTransport': createTransport,
        'AddOperations': AddOperationsToTransport,
        'AddProductToTransport': AddProductToTransport,
        'operation': operation,
        'today': today,
    }
    return render(request, 'product/product-page.html', context)


class ProductAPIList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer