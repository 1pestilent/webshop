from django.db import models
from users.models import User
class CategoryForMan(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'category for man'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class CategoryForWoman(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True,blank=True)

    
    class Meta:
        verbose_name = 'category for woman'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class CategoryForKid(models.Model): 
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'category for kid'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    
class ImagesForProduct(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products_images')

class ImagesForProductCard(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products_images')

class QuantityOfClothes(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    XS = models.PositiveIntegerField(default=0)
    S = models.PositiveIntegerField(default=0)
    M = models.PositiveIntegerField(default=0)
    L = models.PositiveIntegerField(default=0)
    XL = models.PositiveIntegerField(default=0)

class QuantityOfShoes(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    s35 = models.PositiveIntegerField(default=0)
    s36 = models.PositiveIntegerField(default=0)
    s37 = models.PositiveIntegerField(default=0)
    s38 = models.PositiveIntegerField(default=0)
    s39 = models.PositiveIntegerField(default=0)
    s40 = models.PositiveIntegerField(default=0)
    s41 = models.PositiveIntegerField(default=0)
    s42 = models.PositiveIntegerField(default=0)
    s43 = models.PositiveIntegerField(default=0)
    s44 = models.PositiveIntegerField(default=0)
    s45 = models.PositiveIntegerField(default=0)
    s46 = models.PositiveIntegerField(default=0)

class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    text = models.TextField()   
    eval = models.PositiveIntegerField(default=0)
    

