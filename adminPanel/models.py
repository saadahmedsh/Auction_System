from django.db import models

# Create your models here.

class Product(models.Model):
    productName=models.CharField(max_length=100, default=' ')
    imageURL=models.ImageField(upload_to='Images', default='img/icon.png')
    productSpecification=models.CharField(max_length=1000, default=' ')
    productPrice=models.DecimalField(max_digits=10, decimal_places=2)
    productLocation=models.CharField(max_length=100, default=' ')
    productTime=models.DecimalField(max_digits=10, decimal_places=2)



class User(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    status=models.IntegerField(default=0)
    cnic=models.IntegerField(default=0)
    number=models.IntegerField(default=0)







class Order(models.Model):
    user_id=models.IntegerField(default=0)
    product_id=models.IntegerField(default=0)
    bid_price=models.IntegerField(default=0)
    status=models.IntegerField(default=0)



