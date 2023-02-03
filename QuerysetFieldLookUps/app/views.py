from django.shortcuts import render
from app.models import Student
from django.db.models import Avg ,Sum , Count ,Q , Max ,Min
# Create your views here.

def home(request):
    # students=Student.objects.all()
    # students=Student.objects.filter(roll__lt=3)
    # students=Student.objects.filter(roll__lte=3)
    # students=Student.objects.filter(roll__gt=3)
    # students=Student.objects.filter(roll__gte=3)
    # students=Student.objects.filter(roll__exact=3)
    # students=Student.objects.filter(roll__startswith=3)
    # students=Student.objects.filter(roll__gte=3)

    # students=Student.objects.filter(name__contains ='abu')
    # students=Student.objects.filter(name__icontains='Abu')

    #AGGREGATION 
    # students=Student.objects.filter(name__icontains='Abu')
    # average=students.aggregate(Avg('roll'))
    # print(average)
    
    # students=Student.objects.all()
    # average=students.aggregate(Sum('roll'))
    # print(average)
    
    # students=Student.objects.all()
    # average=students.aggregate(Max('roll'))
    # print(average)
    
    # students=Student.objects.all()
    # average=students.aggregate(Min('roll'))
    # print(average) 
    
    
    
    # Q object In DataBase 
    students=Student.objects.filter(Q(roll=1) & Q(name='Abu Bakar Waheed'))
    
    
    print(students.query)
    context ={
        'students':students,
    }
    return render(request, 'index.html',context)