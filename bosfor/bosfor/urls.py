
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index, name="index"),
    path('products/', products, name="products"),
    path('products/page/<int:page>/', products, name="paginator"),
    path('products/<int:gender_id>/', products, name="gender"),
    path('products/<int:gender_id>/<int:category_id>', products, name="gendercat"),
    path('products/product/<int:product_id>/', product, name="product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
