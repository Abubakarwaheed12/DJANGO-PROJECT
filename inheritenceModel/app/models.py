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
    teacher=models.OneToOneField('Teacher', on_delete=models.CASCADE , blank=True , null=True)
    age=None
    
class Teacher(BaseClass):
    grade=models.IntegerField()
    
    #  Our Custom Manager
    teachers=CustomManager()
    # Buit in 
    objects=models.Manager()
    
    
# Many to Many Field

class Publications(models.Model):
    title=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title
    

class Article(models.Model):
    name=models.CharField(max_length=200)
    publications=models.ManyToManyField(Publications)
    
    def __str__(self):
        return self.name