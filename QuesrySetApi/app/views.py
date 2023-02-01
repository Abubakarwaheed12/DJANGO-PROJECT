from django.shortcuts import render
from app.models import Student
# Create your views here.

def index(request):
    # std=Student.objects.all()    
    # std=Student.objects.filter(marks=70)
    # std=Student.objects.exclude(marks=70)
    # for deascending order we will place a - tag in start of field name
    # std=Student.objects.order_by('-name')
    # std=Student.objects.order_by('id')
    # std=Student.objects.reverse()[:2]
    std=Student.objects.values()

    print('SQL query' , std.query)
    context={'students':std}
    return render(request, 'index.html' , context=context)