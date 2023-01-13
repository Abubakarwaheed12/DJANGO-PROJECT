from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField()
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)