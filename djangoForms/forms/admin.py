import email
from pyexpat import model
from django.contrib import admin
from .models import user
# Register your models here.

@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display=['name' , 'email' , 'password',]