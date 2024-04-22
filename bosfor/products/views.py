from django.shortcuts import render, get_object_or_404
from products.models import *

def index(request):
    context = {
        'title': 'Bosfor - главная',
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
    }
    return render(request, 'products/index.html', context)


def products(request, gender_id = None, category_id = None):
    products = Product.objects.all()
    if gender_id:
        products = products.filter(sex_id=gender_id)  
        if category_id:
            products = products.filter(category_id=category_id)
    
    context = {
        'title': 'Bosfor - каталог',
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'title': product.name,
        'product': product,
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
    }
    return render(request, 'products/product.html',context)