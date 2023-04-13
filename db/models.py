from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Customer(models.Model):
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    email = models.TextField(default='')
    mailing_address = models.TextField(default='')
    name = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_date = models.DateField()

class Product(models.Model):
    description = models.TextField(default='')
    name = models.CharField(max_length=40, default='')
    price = models.FloatField()
    product_id = models.CharField(max_length=20, default='')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()