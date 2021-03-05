from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import auth,messages
from django.urls import reverse
from authapp.forms import  UserRegisterForm,UserLoginForm

from authapp.models import  User

# функцияя = вьюхи = контролеры.
def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username , password = password)
            if user and user.is_active:
                auth.login(request,user)
                return HttpResponsePermanentRedirect(reverse('index'))
    else:
        form = UserLoginForm
    context = {
            'title': 'GeekShop - Авторизация',
            'form': form,
        }
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def logout(requst):
    auth.logout(requst)
    return HttpResponsePermanentRedirect(reverse('index'))