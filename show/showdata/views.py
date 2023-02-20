from django.shortcuts import render
from django.db.models import Q
from showdata.models import students , Author , Book , Publisher
# Create your views here.

def studentinfo(request):
    p=Publisher.objects.get(id='1')
    # a=p.authordata.name
    b=Author.objects.get(id=1)
    print(Publisher.objects.get(authordata=b).query)
    # print(a.name)
    st=students.objects.all()
    return render(request , 'student.html' , {'st':st})
