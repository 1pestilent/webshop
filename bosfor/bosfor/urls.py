
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('products/product/', product, name="product"),
    path('products/man/', all_products_for_mans, name="productforman"),
    path('products/woman/', all_products_for_womans, name="productforwoman"),
    path('products/kid/', all_products_for_kids, name="productforkid"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
