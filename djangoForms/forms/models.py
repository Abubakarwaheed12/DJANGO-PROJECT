import email
from statistics import mode
from django.db import models
#  our models for MODEL FORM

class user(models.Model):
    name=models.CharField(max_length=70)
    teacher_name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=70)