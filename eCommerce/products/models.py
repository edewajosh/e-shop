from email.policy import default
from unicodedata import category
from django.db import models
from django.forms import ImageField

class Category(models.Model):
    name = models.CharField(verbose_name='category name', max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name='product category',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product name', max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    previous_price = models.DecimalField(verbose_name='Previous price', max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/products', default='images/default.jpg')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    @property
    def discount(self):
        discount = (self.previous_price - self.price)/self.previous_price * 100
        return discount