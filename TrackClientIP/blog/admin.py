from django.contrib import admin
from .models import post
# Register your models here.

# Decorator Function for displaying the data
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=['id' , 'title' , 'desc']