from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['kod', 'name', 'product', 'email', 'agent', 'contract']
        widgets = {
            'kod': forms.TextInput(attrs={'class': 'popup-content__body-input'}),
            'name': forms.TextInput(attrs={'class': 'popup-content__body-input'}),
            'product': forms.Textarea(attrs={'class': 'popup-content__body-textarea'}),
            'email': forms.EmailInput(attrs={'class': 'popup-content__body-input'}),
            'agent': forms.Select(attrs={'class': 'select-castom'}),
            'contract': forms.Select(attrs={'class': 'select-castom'}),
        }

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['date', 'content', 'category']
        widgets = {
            'date': forms.DateInput(attrs ={'class': 'popup-content__body-input', 'type': 'date'}),
            'content': forms.Textarea(attrs ={'class': 'popup-content__body-textarea'}),
            'category': forms.Select(attrs ={'class': 'select-castom'}),
        }

class AddAppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['date', 'content', 'category', 'doneAppeal', 'client', 'file', 'user_create']
        widgets = {
            'date': forms.DateInput(attrs ={'class': 'popup__create-appeal__body-top-input', 'id': 'popup-appeal__input' ,'type': 'date'}),
            'content': forms.Textarea(attrs ={'class': 'popup__create-appeal__body-bottom-text', 'id': 'popup__create-appeal__body-bottom-text'}),
            'category': forms.Select(attrs ={'class': 'popup__create-appeal__body-top-select', 'id': 'popup-appeal__select'}),
            'doneAppeal': forms.NullBooleanSelect(attrs ={'class': 'popup__create-appeal__body-top-select', 'id': 'popup-appeal__select'}),
            'file': forms.FileInput(attrs={'class': 'popup-history__file'})
        }

class AddAppealItemForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['date', 'content', 'category', 'doneAppeal', 'client', 'file']
        widgets = {
            'date': forms.TextInput(attrs ={'class': 'popup__create-appeal__body-top-input', 'id': 'popup-appeal__input' ,'type': 'date'}),
            'content': forms.Textarea(attrs ={'class': 'popup__create-appeal__body-bottom-text', 'id': 'popup__create-appeal__body-bottom-text'}),
            'category': forms.Select(attrs ={'class': 'popup__create-appeal__body-top-select', 'id': 'popup-appeal__select'}),
            'doneAppeal': forms.NullBooleanSelect(attrs ={'class': 'popup__create-appeal__body-top-select', 'id': 'popup-appeal__select'}),
            'client': forms.HiddenInput()
        }

class AppealCommentsForm(forms.ModelForm):
    class Meta:
        model = AppealComments
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'comment-form_content', 'placeholder': 'Добавить комментрий'}),
            'user': forms.HiddenInput(),
            'file_comment': forms.FileInput(attrs={'class': 'comment-form__file'}),
        }