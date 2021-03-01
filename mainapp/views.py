from django.shortcuts import render
import json
import os


# функцияя = вьюхи = контролеры.
def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать',
        'username': 'Иванов Иван',
    }
    return render(request, 'mainapp/index.html', context)


def CildrenProducts():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    c = os.path.join(BASE_DIR,'mainapp/fixtures/products.json')
    with open( c,'r',encoding='utf8') as json_file:
        return json.load(json_file)



def products(request):

    context = {
        'title': 'GeeKshop',
        'header': 'Каталог',
        'username': 'Иванов Иван',
        'menu': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'},
        ],
        'carousel': [
            {'name': 'First slide', 'way': 'slide-1.jpg', 'starter': True},
            {'name': 'Second slide', 'way': 'slide-2.jpg'},
            {'name': 'Third slide', 'way': 'slide-3.jpg'},
        ],
        'product': CildrenProducts()

    }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать',
        'username': 'Иванов Иван',
        'product': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 500', 'promotion': True},
            {'name': 'Синяя куртка The North Face', 'price': '13 500'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '32 500'},
        ]
    }
    return render(request, 'mainapp/test-context.html', context)