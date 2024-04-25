from django.urls import path

from products.views import *

app_name = 'products'

urlpatterns = [
    path('', products, name="index"),
    path('page/<int:page>/', products, name="paginator"),
    path('<int:gender_id>/', products, name="gender"),
    path('<int:gender_id>/<int:category_id>', products, name="gendercat"),
    path('product/<int:product_id>/', product, name="product"),
]
