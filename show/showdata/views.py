from django.shortcuts import render

from showdata.models import students
# Create your views here.

def studentinfo(request):
    st=students.objects.all()
    return render(request , 'student.html' , {'st':st})
