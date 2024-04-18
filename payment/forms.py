from django import forms
from .models import *

class AddChecksForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'class': 'popup__check-block-item-p-data', 'type': 'date'}),
            'client': forms.HiddenInput(attrs={'class': 'popup__check-block-item-p-data'}),
            'price': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'currency': forms.Select(attrs={'class': 'popup__check-block-item-p-data'}),
            'well': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'wellCheck': forms.Select(attrs={'class': 'popup__check-block-item-p-data'}),
            'wellCommissionUSD': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'commissionPercent': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'commissionUSD': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'commissionRUB': forms.NumberInput(attrs={'class': 'popup__check-block-item-p-data', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'product': forms.Textarea(attrs={'class': 'popup__check__content-p-product'}),
            'status': forms.NullBooleanSelect(attrs={'class': 'popup__check-block-item-p-data'}),
            'ContractNumber': forms.TextInput(attrs={'class': 'popup__check-block-item-p-data', 'list': 'ContractNumber'}),
        }

class AddFileForm(forms.ModelForm):
    class Meta:
        model = CheckFiles
        fields = '__all__'
        widgets = {
            'check_id': forms.HiddenInput(),
            'PathFile': forms.FileInput(attrs={'class': 'file-btn', 'multiple': True})
        }

class AddOperationsForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','class': 'popup-history__input'}),
            'admissionRUB': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Сумма поступления'}),
            'admissionCurrency': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Сумма поступления'}),
            'typeCurrency': forms.Select(attrs={'class': 'popup-history__input'}),
            'nursingRUB': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Затрачено рублей'}),
            'nursingCurrency': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Сумма продажи'}),
            'well': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Курс валюты'}),
            'wellCommission': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Курс коммиссии'}),
            'priceInUSD': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Сумма валюте контракта'}),
            'ReturnPriceUSD': forms.NumberInput(attrs={'class': 'popup-history__input', 'placeholder': 'Сумма возврата по контракту'}),
            'typeLetter': forms.Select(attrs={'class': 'popup-history__input'}),
            'fileOperation': forms.FileInput(attrs={'type': 'file', 'id': 'popup-history__file-letter', 'class': 'popup-history__file string'}),
        }

class AddOperationsToTransport(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['date', 'name', 'check_id', 'productToTransport_id', 'productPriceToPaking', 'productPriceToPakingCurrency', 'productPriceInUSD', 'productPriceInUSDCurrency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','class': 'popup-transport-input'}),
            'name': forms.HiddenInput(),
            'check_id': forms.HiddenInput(attrs={'class': 'input-choice-price_id'}),
            'productToTransport_id': forms.HiddenInput(),
            'productPriceToPaking': forms.NumberInput(attrs={'class': 'input-price-summ', 'placeholder': 'Стоимость по счету'}),
            'productPriceToPakingCurrency': forms.Select(attrs={'class': 'select-price-currency'}),
            'productPriceInUSD': forms.NumberInput(attrs={'class': 'input-price-summ', 'placeholder': 'Стоимость по контракту'}),
            'productPriceInUSDCurrency': forms.Select(attrs={'class': 'select-price-currency'}),
        }