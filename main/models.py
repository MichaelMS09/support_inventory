from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    amount = models.IntegerField(null=True)
    stok = models.IntegerField(null=True)