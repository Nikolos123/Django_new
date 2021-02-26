from django.shortcuts import render

# функцияя = вьюхи = контролеры.
def index(request):
   return render(request, 'mainapp/index.html')

def products(request):
   return render(request, 'mainapp/products.html')