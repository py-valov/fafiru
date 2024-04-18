from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django import forms

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
       'class': 'form-input',
       'placeholder': 'Введите логин'
       }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
       'class': 'form-input',
       'placeholder': 'Введите пароль'
       }))

    class Meta:
      model = Users
      fields = {'username', 'password'}


class RegistrationForm(UserCreationForm):
   class Meta:
      model = Users
      fields = {'first_name', 'last_name', 'username', 'email', 'password1', 'password2'}
