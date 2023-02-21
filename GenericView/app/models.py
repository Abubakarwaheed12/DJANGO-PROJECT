from django.db import models

# Create your models here.

class patient(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=10)

    
    def __str__(self):
        return self.name