from django.shortcuts import render, get_object_or_404
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
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

def all_products_for_mans(request):
    context = {
        'title': 'Bosfor - товары для мужчин',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': Product.objects.filter(sex__name='Мужской'),
    }
    return render(request, 'products/products.html', context)

def all_products_for_womans(request):
    context = {
        'title': 'Bosfor - товары для женщин',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': Product.objects.filter(sex__name='Женский'),
    }
    return render(request, 'products/products.html', context)

def all_products_for_kids(request):
    context = {
        'title': 'Bosfor - товары для детей',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': Product.objects.filter(sex__name='Дети'),
    }
    return render(request, 'products/products.html', context)

def category_products_for_man(request, category_id):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=category, sex__name='Мужской')
    else:
        products = Product.objects.filter(sex__name='Мужской')
    
    context = {
        'title': 'Bosfor - товары для мужчин',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': products,
    }
    return render(request, 'products/products.html', context)

def category_products_for_woman(request, category_id):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=category, sex__name='Женский')
    else:
        products = Product.objects.filter(sex__name='Женский')
    
    context = {
        'title': 'Bosfor - товары для женщин',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': products,
    }
    return render(request, 'products/products.html', context)

def category_products_for_kid(request, category_id):
    if category_id:
        category = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=category, sex__name='Дети')
    else:
        products = Product.objects.filter(sex__name='Дети')
    
    context = {
        'title': 'Bosfor - товары для детей',
        'man_categorys': Category.objects.filter(product__sex__name='Мужской').distinct(),
        'woman_categorys': Category.objects.filter(product__sex__name='Женский').distinct(),
        'kid_categorys': Category.objects.filter(product__sex__name='Дети').distinct(),
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product(request):
    return render(request, 'products/product.html')