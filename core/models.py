from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True, blank=True)
    
class Account(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    created_at = models.DateTimeField(null=True, blank=True)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    
class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    