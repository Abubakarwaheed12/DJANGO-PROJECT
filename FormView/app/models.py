from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name=models.CharField(max_length=200)
    message=models.CharField(max_length=2112)
    
    
    def __str__(self):
        return f'{self.name} ({self.message}) '
    
