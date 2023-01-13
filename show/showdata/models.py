from django.db import models

# Create your models here.
class students(models.Model):
    stuid=models.IntegerField()
    name=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    password=models.CharField(max_length=70)

# register this model in admin interface function must be inside the class
    # def __str__(self):
    #     return self.name
