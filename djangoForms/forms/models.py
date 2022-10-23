import email
from django.db import models
#  our models for MODEL FORM

class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=70)