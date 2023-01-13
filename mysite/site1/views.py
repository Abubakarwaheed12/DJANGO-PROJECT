from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

# def home(request):
#     return HttpResponse("home page")

# NOW RENDER THE TEMPLATE FILES 
def home(request):
    return render(request, 'webify/index.html')
def about(request):
    return render(request, 'webify/about.html', {'a':'/about'})
def services(request):
    return render(request, 'webify/services.html', {'ab':'webify/services'} )
# third argument in view function
# ,{'ab':'/services'}
#  DYNAMIC View Functio 
# | PIPE IS USED TO FILTER
# ex {{variable|filter }}
# ex {{name|upper }}
# Multiple filters 
# ex {{name|upper|filter }}
def dynamic(request):
    name='abu bakar waheed'
    age=False
    city='Muridkey'
    d=datetime.now()
    students=['abu bakar' , 'talha' ,' ubaid', 'saad']
    # empty list
    student=[]
    details={'name':name, 'age':age, 'city':city, 'd':d,'students':students,'student':student}
    return render(request, 'webify/dynamic.html', details)


# VIEW FOR HOME PAGE AND TEMPLATE INSIDE THE PROJECT
def hah(request):
    return render(request,'index.html')