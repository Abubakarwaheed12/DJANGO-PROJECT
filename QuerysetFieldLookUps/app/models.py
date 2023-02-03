from django.db import models
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField(unique=True)
    city=models.CharField(max_length=200)   
    pass_date=models.DateField()
    adm_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
