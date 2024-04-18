from django import forms
from .models import *

class CreateTransport(forms.ModelForm):
    class Meta:
      model = Transports
      fields = '__all__'
      widgets = {
         'date_create': forms.DateInput(attrs={'class': 'popup__create-transport__body-input', 'type': 'date'}),
         'name': forms.TextInput(attrs={'class': 'popup__create-transport__body-input', 'type': 'text'}),
         'category': forms.Select(attrs={'class': 'popup__create-transport__body-input'}),
         'region': forms.TextInput(attrs={'class': 'popup__create-transport__body-input', 'type': 'text'}),
         'status': forms.HiddenInput(attrs={'class': 'popup__create-transport__body-input'}),
      }