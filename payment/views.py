from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics
from os.path import basename
from datetime import date
from django.db.models import Q, Sum

from .models import *
from .serializers import *
from .forms import *
from main.models import Clients, Appeal
from main.forms import AddAppealForm
from product.models import Products

@login_required
def Finance(request):
    

    checkClient = Clients.objects.all()
    context = {
        'title': 'Оплаты | Fafiru',
        'checkClient': checkClient,
    }

    return render(request, 'payment/finance.html', context)

@login_required
def Payment(request, payment_id):
    check = Check.objects.get(pk=payment_id)
    checkFile = CheckFiles.objects.filter(check_id=payment_id)

    if request.method == 'POST':
        if request.POST['typeForm'] == 'newCheck':
          checkForm = AddChecksForm(request.POST, instance=check)
          operationForm = AddOperationsForm()
          checkFiles = AddFileForm()
          if checkForm.is_valid():
              checkForm.save()
              idCheck = checkForm.save().id
              check_id = Check.objects.get(pk=idCheck)

              if request.FILES:
                checkFiles = AddFileForm(request.POST, request.FILES, instance=check)
                files = request.FILES.getlist('PathFile')
                if checkFiles.is_valid():
                    for fl in files:
                        flItem = CheckFiles(check_id = check_id, PathFile = fl)
                        flItem.save()
              else:
                checkFiles = AddFileForm()

              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          else:
              print('Не получилось')
    else:
      operationForm = AddOperationsForm()
      checkForm = AddChecksForm(instance=check)
      checkFiles = AddFileForm()

    if request.method == 'POST':
        if request.POST['typeForm'] == 'newOper':
          operationForm = AddOperationsForm(request.POST, request.FILES)
          checkForm = AddChecksForm()
          checkFiles = AddFileForm()
          if operationForm.is_valid():
              operationForm.save()

              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
        operationForm = AddOperationsForm()
        checkForm = AddChecksForm(instance=check)
        checkFiles = AddFileForm()

    if request.method == 'POST':
        if request.POST['typeForm'] == 'DeleteFile':
          operationForm = AddOperationsForm(request.POST)
          fileItem = CheckFiles.objects.get(id=operationForm.data['id'])
          checkForm = AddChecksForm()
          checkFiles = AddFileForm()
          fileItem.PathFile.delete(save=True)
          fileItem.delete()
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    else:
        operationForm = AddOperationsForm()
        checkForm = AddChecksForm(instance=check)
        checkFiles = AddFileForm()

    if request.method == 'POST':
        if request.POST['typeForm'] == 'newAppeal':
          formAppealMethod = AddAppealForm(request.POST)
          checkForm = AddChecksForm()
          checkFiles = AddFileForm()
          operationForm = AddOperationsForm()
          if formAppealMethod.is_valid() or checkForm.is_valid():
              formAppealMethod.save()
              appeal = formAppealMethod.save().id
              checkAppeal = Check.objects.filter(pk=payment_id).update(appeal_id=appeal)
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          
    else:
        operationForm = AddOperationsForm()
        checkForm = AddChecksForm(instance=check)
        checkFiles = AddFileForm()

    
    
    operations = Operation.objects.filter(check_id=payment_id)
    operationsCount = operations.count()

    # Сумма счета
    summCheck = 0
    
    if check.commissionPercent and check.commissionUSD and check.commissionRUB:
        summCheck = check.price * check.well / check.commissionPercent + check.commissionUSD * check.wellCommissionUSD + check.commissionRUB
    elif check.commissionPercent and check.commissionUSD:
        summCheck = check.price * check.well / check.commissionPercent + check.commissionUSD * check.wellCommissionUSD
    elif check.commissionPercent and check.commissionRUB:
        summCheck = check.price * check.well / check.commissionPercent + check.commissionRUB
    elif check.commissionUSD and check.commissionRUB:
        summCheck = check.price * check.well + check.commissionUSD * check.wellCommissionUSD + check.commissionRUB
    elif check.commissionPercent:
        summCheck = check.price * check.well / check.commissionPercent
    elif check.commissionUSD:
        summCheck = check.price * check.well + check.commissionUSD * check.wellCommissionUSD
    elif check.commissionRUB:
        summCheck = check.price * check.well + check.commissionRUB


    

    # Сумма поступлений от клиента
    operationAdmissionRUB = operations.filter(name='Поступление')
    operAdmisRUB = 0

    for OARUB in operationAdmissionRUB:
        operAdmisRUB += OARUB.admissionRUB

    # Сумма наших затрат по оплате
    summNursingRUB = 0
    SUMM_COMMISSION = 0
    
    # Сумма валют на балансе по счету
    summUSD = 0
    summCNY = 0
    summEUR = 0

    # Сумма выкупленного товар
    priceProduct = 0
    priceDelivery = 0
    for oper in operations:
        if oper.nursingRUB:
          summNursingRUB += oper.nursingRUB

        if oper.name == 'Продажа':
           summNursingRUB -= oper.admissionRUB

        # Расчет комиссии при оплате
        if oper.name == "Оплата":
            if check.commissionPercent and check.commissionUSD and check.commissionRUB:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well / check.commissionPercent + check.commissionUSD * oper.wellCommission + check.commissionRUB - oper.nursingCurrency * oper.well
            elif check.commissionPercent and check.commissionUSD:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well / check.commissionPercent + check.commissionUSD * oper.wellCommission - oper.nursingCurrency * oper.well
            elif check.commissionPercent and check.commissionRUB:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well / check.commissionPercent + check.commissionRUB - oper.nursingCurrency * oper.well
            elif check.commissionUSD and check.commissionRUB:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well + check.commissionUSD * oper.wellCommission + check.commissionRUB - oper.nursingCurrency * oper.well
            elif check.commissionPercent:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well / check.commissionPercent - oper.nursingCurrency * oper.well
            elif check.commissionUSD:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well + check.commissionUSD * oper.wellCommission - oper.nursingCurrency * oper.well
            elif check.commissionRUB:
               SUMM_COMMISSION += oper.nursingCurrency * oper.well + check.commissionRUB - oper.nursingCurrency * oper.well

            if oper.priceInUSD:
               priceProduct += oper.priceInUSD
        elif oper.name == "Возврат":
            if oper.ReturnPriceUSD:
               priceProduct -= oper.ReturnPriceUSD

        elif oper.name == "Провоз":
            if oper.productPriceInUSD:
               priceDelivery += oper.productPriceInUSD
        

        if oper.typeCurrency == "$":
            if oper.admissionCurrency:
              summUSD += oper.admissionCurrency
            elif oper.nursingCurrency:
              summUSD -= oper.nursingCurrency
        if oper.typeCurrency == "¥":
            if oper.admissionCurrency:
              summCNY += oper.admissionCurrency
            elif oper.nursingCurrency:
              summCNY -= oper.nursingCurrency
        if oper.typeCurrency == "€":
            if oper.admissionCurrency:
              summEUR += oper.admissionCurrency
            elif oper.nursingCurrency:
              summEUR -= oper.nursingCurrency

    priceBalance = priceProduct - priceDelivery
    expenses = summNursingRUB + SUMM_COMMISSION
    balance = operAdmisRUB - expenses
    today = date.today()
    
    context = {
        'title': f'Платеж {check.currency} | Fafiru',
        'check': check,
        'checkFile': checkFile,
        'operationForm': operationForm,
        'operations': operations,
        'operationsCount': operationsCount,
        'operAdmisRUB': operAdmisRUB,
        'summCheck': summCheck,
        'expenses': expenses,
        'balance': balance,
        'summUSD': summUSD,
        'summCNY': summCNY,
        'summEUR': summEUR,
        'priceProduct': priceProduct,
        'priceDelivery': priceDelivery,
        'priceBalance': priceBalance,
        'summCommission': SUMM_COMMISSION,
        'checkForm': checkForm,
        'checkFiles': checkFiles,
        'today': today,
    }
    return render(request, 'payment/finance-page.html', context)


def Balance(request):
    totalPositive = 0
    totalNegative =0
    info = []
    if request.method == 'POST':
       if request.POST['type'] == 'SelectBalance':
          if request.POST['typeBalance'] == 'Баланс контракта':
            client = Clients.objects.all().order_by('-pk')
            contract = request.POST['contract']
            typeBalance = 'Баланс контракта'

            for clientItem in client:
                OperPrice = Operation.objects.filter(check_id__client_id=clientItem, check_id__ContractNumber=request.POST['contract'], name='Оплата').aggregate(OperPrice=Sum('priceInUSD'))
                ReturnPrice = Operation.objects.filter(check_id__client_id=clientItem, check_id__ContractNumber=request.POST['contract'], name='Возврат').aggregate(ReturnPrice=Sum('ReturnPriceUSD'))
                DeliveryPrice = Operation.objects.filter(check_id__client_id=clientItem, check_id__ContractNumber=request.POST['contract'], name='Провоз').aggregate(DeliveryPrice=Sum('productPriceInUSD'))

                if OperPrice['OperPrice'] == None and ReturnPrice['ReturnPrice'] == None:
                   totalPrice = 0
                elif OperPrice['OperPrice'] == None:
                   totalPrice = 0 - ReturnPrice['ReturnPrice']
                elif ReturnPrice['ReturnPrice'] == None:
                   totalPrice = OperPrice['OperPrice'] - 0
                else:
                   totalPrice = OperPrice['OperPrice'] - ReturnPrice['ReturnPrice']
                
                if DeliveryPrice['DeliveryPrice'] == None:
                   Balance = totalPrice - 0
                   totalDelivery = 0
                else:
                   Balance = totalPrice - DeliveryPrice['DeliveryPrice']
                   totalDelivery = DeliveryPrice['DeliveryPrice']

                if totalPrice == 0 and DeliveryPrice['DeliveryPrice'] == None and Balance == 0:
                    continue

                info.append({
                   'client': clientItem,
                   'price': totalPrice,
                   'delivery': totalDelivery,
                   'balance': Balance
                   })
                
                totalPositive += totalPrice
                totalNegative += totalDelivery

          if request.POST['typeBalance'] == 'Валютный баланс':
            client = Clients.objects.filter(kod__icontains=request.POST['kodClient'])
            contract = request.POST['contract']
            typeBalance = 'Валютный баланс'
            if request.POST['kodClient'] == '':
               contract = ''
               typeBalance = ''
               client = ''
            
            else:
                try:
                    oper = Operation.objects.filter(check_id__client_id=client[0], check_id__ContractNumber=contract ,name__in=['Оплата', 'Возврат', 'Провоз'])

                    Balance = 0
                    for o in oper:
                        if o.name == 'Оплата':
                            Balance += o.priceInUSD
                            totalPositive += o.priceInUSD
                            info.append({
                            'date': o.date,
                            'price': o.priceInUSD,
                            'delivery': '',
                            'balance': Balance,
                            'comment': o.name
                            })
                        if o.name == 'Возврат':
                            Balance -= o.ReturnPriceUSD
                            totalPositive -= o.ReturnPriceUSD
                            info.append({
                            'date': o.date,
                            'price': '',
                            'delivery': o.ReturnPriceUSD,
                            'balance': Balance,
                            'comment': o.name
                            })
                        if o.name == 'Провоз':
                            Balance -= o.productPriceInUSD
                            totalNegative += o.productPriceInUSD
                            info.append({
                            'date': o.date,
                            'price': '',
                            'delivery': o.productPriceInUSD,
                            'balance': Balance,
                            'comment': o.name
                            })
                except:
                    info.append({
                        'date': '',
                        'price': '',
                        'delivery': '',
                        'balance': '',
                        'comment': ''
                        })
                

    else:
       contract = ''
       typeBalance = ''
       client = ''

    totalBalance = totalPositive - totalNegative

    context = {
        'title': 'Баланс | Fafiru',
        'totalPositive': totalPositive,
        'totalNegative': totalNegative,
        'totalBalance': totalBalance,
        'typeBalance': typeBalance,
        'info': info,
        'contract': contract,
        'client': client,
    }

    return render(request, 'payment/finance-balance.html', context)

class ChecksAPIList(generics.ListAPIView):
    queryset = Check.objects.all()
    serializer_class = ChecksSerializer

class ChecksNoPaymentAPIList(generics.ListAPIView):
    queryset = Check.objects.filter(status = False)
    serializer_class = ChecksSerializer


class OperationsAPIList(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationsSerializer