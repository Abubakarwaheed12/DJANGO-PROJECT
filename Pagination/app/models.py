from django.db import models

# Create your models here.

class post(models.Model):
    name=models.CharField(max_length=190)
    title=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name 