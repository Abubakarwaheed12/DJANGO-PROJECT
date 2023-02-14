from django.contrib import admin
from app.models import Student , Teacher , Publications , Article
# Register your models here.
# admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Article)
admin.site.register(Publications)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id' , 'name' , 'rollNo' , 'city']
    
  
# Program 1 
# a='abubakarwaheed'
# # count a in string 
# def countchar(str):
#     countch=0
#     for i in str:
#         if i=='e':
#             countch +=1
#     return countch
# print(countchar(a))  
    
    

# Program 2
# l=[]
# stri='pynative'
# for i in stri:
#     a=stri.index(i)
#     if a%2==0:
#         l.append(stri[a])
# new_str=''.join(l)
# print(new_str)




# Program 3
# a='10010010000010001'
# # find consective zeros 
# def findConsective(str):
#     l=str.split('1')
#     a=len(max(l))
#     print(5)
# findConsective(a)