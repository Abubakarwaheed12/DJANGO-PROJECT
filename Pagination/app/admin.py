from django.contrib import admin
from app.models import post 
# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=['id','name' , 'title']