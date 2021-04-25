from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from mainapp.models import  ProductCategory,Product

# функцияя = вьюхи = контролеры.
def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать',
        'username': 'Иванов Иван',
    }
    return render(request, 'mainapp/index.html', context)


def products(request,category_id=None,page=1):

    context = {
        'title': 'GeeKshop',
        'header': 'Каталог',
        'menu': ProductCategory.objects.all(),
        'carousel': [
            {'name': 'First slide', 'way': 'slide-1.jpg', 'starter': True},
            {'name': 'Second slide', 'way': 'slide-2.jpg'},
            {'name': 'Third slide', 'way': 'slide-3.jpg'},
        ],
        # 'product': Product.objects.all()

    }
    if category_id:
        products = Product.objects.filter(category_id = category_id).order_by('name')
    else:
        products = Product.objects.all().order_by('name')
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page)
    context.update({'product':products_paginator})
    return render(request, 'mainapp/products.html', context)

# class ProductListByCategory(ListView):
#     """
#     Контроллер вывода списка товаров
#     """
#     model = Product
#     template_name = 'mainapp/products.html'
#     context_object_name = 'products'
#
#     def get_context_data(self, category_id=None, *args, **kwargs):
#         """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
#
#         context = super().get_context_data()
#         context['categories'] = ProductCategory.objects.all()
#
#         if self.kwargs.get('category_id'):
#             category_id = int(self.kwargs.get('category_id'))
#             products = Product.objects.filter(category_id=category_id).order_by('-price')
#         else:
#             products = Product.objects.all().order_by('-price')
#         context['products'] = products
#
#         return context


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""

        context = super().get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


# def products_ajax(request, pk=None, page=1):
#    if request.is_ajax():
#        links_menu = get_links_menu()
#
#        if pk:
#            if pk == '0':
#                category = {
#                    'pk': 0,
#                    'name': 'все'
#                }
#                products = get_products_orederd_by_price()
#            else:
#                category = get_category(pk)
#                products = get_products_in_category_orederd_by_price(pk)
#
#            paginator = Paginator(products, 2)
#            try:
#                products_paginator = paginator.page(page)
#            except PageNotAnInteger:
#                products_paginator = paginator.page(1)
#            except EmptyPage:
#                products_paginator = paginator.page(paginator.num_pages)
#
#            content = {
#                'links_menu': links_menu,
#                'category': category,
#                'products': products_paginator,
#            }
#
#            result = render_to_string(
#                         'mainapp/includes/inc_products_list_content.html',
#                         context=content,
#                         request=request)
#
#            return JsonResponse({'result': result})