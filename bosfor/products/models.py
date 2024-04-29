from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True, default='Описание отсутствует')
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=32, unique=True, null=True)

    class Meta:
        verbose_name = 'gender'
        verbose_name_plural = 'genders'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sex = models.ForeignKey(Gender, on_delete=models.PROTECT)
    image_for_card = models.ImageField(upload_to='products_images', null=True, blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name} | Пол: {self.sex.name}'
        
class ImagesForProduct(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products_images')

class QuantityOfClothes(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    XSS = models.PositiveIntegerField(default=0)
    XS = models.PositiveIntegerField(default=0)
    S = models.PositiveIntegerField(default=0)
    M = models.PositiveIntegerField(default=0)
    L = models.PositiveIntegerField(default=0)
    XL = models.PositiveIntegerField(default=0)
    XXL = models.PositiveIntegerField(default=0)
    XXL = models.PositiveIntegerField(default=0)
    ONESIZE = models.PositiveIntegerField(default=0)

class QuantityOfShoes(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    s28 = models.PositiveIntegerField(default=0)
    s29 = models.PositiveIntegerField(default=0)
    s30 = models.PositiveIntegerField(default=0)
    s31 = models.PositiveIntegerField(default=0)
    s32 = models.PositiveIntegerField(default=0)
    s33 = models.PositiveIntegerField(default=0)
    s34 = models.PositiveIntegerField(default=0)
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

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    
    def total_quantity(self):
        return sum(basket.quantity for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    timpestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()
    
    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

class Status(models.Model):
    name = models.CharField(32)

    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,on_delete=models.PROTECT)
    sum = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'Заказ №{self.id} от {self.user.email}'

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'Товар к заказу №{self.id}'
