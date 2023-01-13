import re
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def student(request, my_id):
    if my_id==1:
        name="abu bakar"
    return render(request , 'student.html' , {'id':my_id})