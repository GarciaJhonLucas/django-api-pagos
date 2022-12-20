from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)