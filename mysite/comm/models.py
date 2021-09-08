from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING, SET_NULL

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    picture = models.ImageField(null=True, max_length=255, upload_to='productPictures')
    cart = models.ForeignKey(Cart, on_delete=SET_NULL, null=True)