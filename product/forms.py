from django import forms
from .models import *

class AddProducts(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'class': 'popup-stock-input', 'type': 'date'}),
            'client_id': forms.HiddenInput(attrs={'class': 'input-client-id'}),
            'namePaking': forms.TextInput(attrs={'class': 'popup-stock-input'}),
            'weight': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'volume': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'price': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'transport': forms.Select(attrs={'class': 'popup-stock-input'}),
            'ContractNumber': forms.TextInput(attrs={'class': 'popup-stock-input'}),
            'nameProduct': forms.Textarea(attrs={'class': 'popup-stock-product'}),
            'category': forms.Select(attrs={'class': 'popup-stock-input'}),
            'currency': forms.Select(attrs={'class': 'popup-stock-input'}),
            'status': forms.HiddenInput()
        }

class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'class': 'popup-stock-input', 'type': 'date'}),
            'client_id': forms.HiddenInput(attrs={'class': 'input-client-id'}),
            'namePaking': forms.TextInput(attrs={'class': 'popup-stock-input'}),
            'weight': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'volume': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'price': forms.NumberInput(attrs={'class': 'popup-stock-input', 'pattern': "\d+(\.\d{2})?", 'title': '2.10 (2 "точка" 10) - два знака после точки'}),
            'transport': forms.Select(attrs={'class': 'popup-stock-input'}),
            'ContractNumber': forms.HiddenInput(attrs={'class': 'popup-stock-input'}),
            'weightBalance': forms.HiddenInput(attrs={'class': 'popup-stock-input'}),
            'volumeBalance': forms.HiddenInput(attrs={'class': 'popup-stock-input'}),
            'priceBalance': forms.HiddenInput(attrs={'class': 'popup-stock-input'}),
            'nameProduct': forms.Textarea(attrs={'class': 'popup-stock-product'}),
            'category': forms.Select(attrs={'class': 'popup-stock-input'}),
            'currency': forms.Select(attrs={'class': 'popup-stock-input'}),
            'status': forms.Select(attrs={'class': 'popup-stock-input'})
        }

class AddComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        widgets = {
            'product_id': forms.HiddenInput(),
            'comment': forms.Textarea(attrs={'class': 'item-head__comment-text'})
        }

class AddFileProduct(forms.ModelForm):
    class Meta:
        model = ProductFiles
        fields = '__all__'
        widgets = {
            'product_id': forms.HiddenInput(),
            'file': forms.FileInput(attrs={'class': 'file-btn', 'multiple': True})
        }

class AddProductToTransportForm(forms.ModelForm):
    class Meta:
        model = ProductToTransport
        fields = '__all__'
        widgets = {
            'transport_id': forms.HiddenInput(attrs={'class': 'popup-transport-input-id input-transport-id'}),
            'product_id': forms.HiddenInput(),
            'weight': forms.NumberInput(attrs={'class': 'popup-transport-input input-body-150'}),
            'volume': forms.NumberInput(attrs={'class': 'popup-transport-input input-body-150'}),
            'comments': forms.Textarea(attrs={'class': 'popup-transport-input__product'}),
        }