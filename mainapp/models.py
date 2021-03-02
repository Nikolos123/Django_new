from django.db import models
import json
import os


# Create your models here.
class ProductCategory(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    # def OneStartCategory(self):
    #     a = [
    #         {'name': 'Новинки', 'description': 'Новая одежда'},
    #         {'name': 'Одежда', 'description': 'Новая одежда'},
    #         {'name': 'Обувь', 'description': 'Новая одежда'},
    #         {'name': 'Аксессуары', 'description': 'Новая одежда'},
    #         {'name': 'Подарки', 'description': 'Новая одежда'},
    #     ]
    #     for i in a:
    #         ProductCategory.objects.create(name=i['name'], description=i['description'])


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # PROTECT
    status_buy = models.CharField(max_length=64, default='Отправить в корзину')


# def OneStartProduct(self):
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     c = os.path.join(BASE_DIR, 'mainapp/fixtures/products.json')
#     with open(c, 'r', encoding='utf8') as json_file:
#         products = json.load(json_file)
#
#     for i in products:
#         ProductCategory.objects.create(name=i['name'], short_description=i['info'],price=['price'], quantity = 10, status_buy= ['status'],image = ['way'])

def __str__(self):
    return f'{self.name} | {self.category.name}'
