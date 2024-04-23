from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, F, Case, When
from django.core.paginator import Paginator
from products.models import *


def index(request):
    context = {
        'title': 'Bosfor - главная',
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
    }
    return render(request, 'products/index.html', context)


def products(request, gender_id = None, category_id = None, page=1):
    products = Product.objects.annotate(
    total_quantity=Sum(
                Case(
                    When(
                        quantityofclothes__XS__gt=0, then=F('quantityofclothes__XS')
                    ),
                    When(
                        quantityofclothes__S__gt=0, then=F('quantityofclothes__S')
                    ),
                    When(
                        quantityofclothes__M__gt=0, then=F('quantityofclothes__M')
                    ),
                    When(
                        quantityofclothes__L__gt=0, then=F('quantityofclothes__L')
                    ),
                    When(
                        quantityofclothes__XL__gt=0, then=F('quantityofclothes__XL')
                    ),
                    default=0
                ) +
                Case(
                    When(
                        quantityofshoes__s35__gt=0, then=F('quantityofshoes__s35')
                    ),
                    When(
                        quantityofshoes__s36__gt=0, then=F('quantityofshoes__s36')
                    ),
                    When(
                        quantityofshoes__s37__gt=0, then=F('quantityofshoes__s37')
                    ),
                    When(
                        quantityofshoes__s38__gt=0, then=F('quantityofshoes__s38')
                    ),
                    When(
                        quantityofshoes__s39__gt=0, then=F('quantityofshoes__s39')
                    ),
                    When(
                        quantityofshoes__s40__gt=0, then=F('quantityofshoes__s40')
                    ),
                    When(
                        quantityofshoes__s41__gt=0, then=F('quantityofshoes__s41')
                    ),
                    When(
                        quantityofshoes__s42__gt=0, then=F('quantityofshoes__s42')
                    ),
                    When(
                        quantityofshoes__s43__gt=0, then=F('quantityofshoes__s43')
                    ),
                    When(
                        quantityofshoes__s44__gt=0, then=F('quantityofshoes__s44')
                    ),
                    When(
                        quantityofshoes__s45__gt=0, then=F('quantityofshoes__s45')
                    ),
                    When(
                        quantityofshoes__s46__gt=0, then=F('quantityofshoes__s46')
                    ),
                    default=0
                )
            )
        ).filter(total_quantity__gt=0)
    
    if gender_id:
        products = products.filter(sex_id=gender_id)  
        if category_id:
            products = products.filter(category_id=category_id)
    
    per_page = 12 
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)  

    context = {
        'title': 'Bosfor - каталог',
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context)

def product(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)

    try:
        quantity_of_clothes = QuantityOfClothes.objects.get(product=product)
    except QuantityOfClothes.DoesNotExist:
        quantity_of_clothes = None
    
    if quantity_of_clothes is None:
        quantity_of_shoes = QuantityOfShoes.objects.get(product=product)
    else:
        quantity_of_shoes = None

    context = {
        'title': product.name,
        'product': product,
        'genders': Gender.objects.all(),
        'categories': Category.objects.filter().distinct(),
        'quantity_of_clothes': quantity_of_clothes,
        'quantity_of_shoes': quantity_of_shoes,
    }
    return render(request, 'products/product.html',context)