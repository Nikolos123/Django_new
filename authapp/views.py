from django.shortcuts import render

from authapp.models import  User

# функцияя = вьюхи = контролеры.
def login(request):
    context = {
        'title': 'GeekShop - Авторизация',
        # 'header': 'Добро пожаловать',
        # 'username': 'Иванов Иван',
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'GeekShop - Регистрация',
        # 'header': 'Добро пожаловать',
        # 'username': 'Иванов Иван',
    }
    return render(request, 'authapp/register.html', context)
