from django.shortcuts import render
from products.models import *

def index(request):
    context = {
        'title': 'Bosfor - главная',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
    'title': 'Bosfor - каталог',
    'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

def all_products_for_mans(request):
    context = {
        'title': 'Bosfor - товары для мужчин',
        'products': Product.objects.filter(sex__name='Мужской'),
    }
    return render(request, 'products/products.html', context)

def all_products_for_womans(request):
    context = {
        'title': 'Bosfor - товары для мужчин',
        'products': Product.objects.filter(sex__name='Женский'),
    }
    return render(request, 'products/products.html', context)

def all_products_for_kids(request):
    context = {
        'title': 'Bosfor - товары для мужчин',
        'products': Product.objects.filter(sex__name='Дети'),
    }
    return render(request, 'products/products.html', context)



def product(request):
    return render(request, 'products/product.html')