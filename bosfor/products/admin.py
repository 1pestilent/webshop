from django.contrib import admin
from products.models import *

admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(ImagesForProduct)


class QuantityOfClothesInline(admin.TabularInline):
    model = QuantityOfClothes
    extra = 0

class QuantityOfShoesInline(admin.TabularInline):
    model = QuantityOfShoes
    extra = 0

class ImagesForProductInline(admin.TabularInline):
    model = ImagesForProduct
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    inlines = [QuantityOfClothesInline, QuantityOfShoesInline, ImagesForProductInline]
    list_display = ['name','sex','category','price']
    list_filter = ['sex','category']
    fields = ('name', 'description',('price','category','sex'),'image_for_card')
    search_fields = ('name',)
    ordering = ('name', )

admin.site.register(Product, ProductAdmin)
