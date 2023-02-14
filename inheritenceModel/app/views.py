from django.shortcuts import render
from app.models import Student , Teacher
# Create your views here.

def home(request):
    t=Teacher.teachers.all()
    t=Teacher.objects.all()
    # print(t[1].name)
    return render(request, 'index.html')