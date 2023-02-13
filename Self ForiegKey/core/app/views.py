from django.shortcuts import render
from app.models import Teachers
# Create your views here.

def home(request):
    t=Teachers.objects.filter(headOfDepartment__name='Ashraf Ali')
    print(t)
    context={
        'tachers':t,
    }
    return render(request, 'index.html' , context)
