import email
from pyexpat import model
from django.db import models

# Create your models here.

class user_form(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


