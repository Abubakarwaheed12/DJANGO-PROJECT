from django.db import models
from app.managers import CustomManager
# Create your models here.

class BaseClass(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    
    class Meta:
        abstract=True
        
        
class Student(BaseClass):
    rollNo=models.IntegerField()
    age=None
    
class Teacher(BaseClass):
    grade=models.IntegerField()
    
    #  Our Custom Manager
    teachers=CustomManager()
    # Buit in 
    objects=models.Manager()