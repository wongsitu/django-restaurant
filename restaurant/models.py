from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100,unique=True,blank=False)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField()

class Dishe(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    price = models.PositiveSmallIntegerField()
    image_url = models.URLField()
    description = models.TextField(max_length=100, blank=True)

class Order(models.Model):
    paymentMethod = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    dishes = models.ForeignKey(Dishe, on_delete=models.CASCADE, related_name='dishes')

