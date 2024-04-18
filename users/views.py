from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegistrationForm
from .models import Users

def Authorization(request):
    if request.method == 'POST':
        login = LoginForm(data=request.POST)
        if login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('home')
    else:
        login = LoginForm()

    
    
    context = {
        'title': "Авторизация | Fafiru",
        'login': login,
    }

    return render(request, 'users/authorization.html', context)

def Registration(request):
    if request.user.is_superuser:

      if request.method == 'POST':
          form = RegistrationForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')
      else:
        form = RegistrationForm()
      context = {
          'title': 'Регистрация',
          'form': form,
      } 

      return render(request, 'users/registration.html', context)
    else:
        return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('authorization')