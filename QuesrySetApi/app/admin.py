from django.contrib import admin
from app.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'roll','city' , 'marks' , 'pass_date']
