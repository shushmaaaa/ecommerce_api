from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username


class Shipping(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    
    
    def __str__(self):
        return self.user.username +" "+ self.address