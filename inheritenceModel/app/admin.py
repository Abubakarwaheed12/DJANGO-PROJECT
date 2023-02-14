from django.contrib import admin
from app.models import Student , Teacher
# Register your models here.
# admin.site.register(Student)
admin.site.register(Teacher)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id' , 'name' , 'rollNo' , 'city']
    
    
    
    
    
    




# Program 
# l=[]
# str='pynative'
# for i in str:
#     a=str.index(i)
#     if a%2==0:
#         l.append(str[a])
# for val in l:
#     print(f'{val}')