import re
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def student(request, my_id):
    
    return render(request , 'student.html' , {'id':my_id})