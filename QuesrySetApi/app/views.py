from django.shortcuts import render
from app.models import Student
# Create your views here.

def index(request):
    #QUERY SET METHODS TAHT RETURN NEW QUERY SET  
    
    # std=Student.objects.all()    
    # std=Student.objects.filter(marks=70)
    # std=Student.objects.exclude(marks=70)
    # for deascending order we will place a - tag in start of field name
    # std=Student.objects.order_by('-name')
    # std=Student.objects.order_by('id')
    # std=Student.objects.reverse()[:2]
    # std=Student.objects.values()
    # std=Student.objects.values_list(flat=True)

    # std=Student.objects.using('default')
    # std=Student.objects.dates('pass_date', 'year')

    std=Student.objects.all()
    print(std)
    print('SQL query' , std.query)
    context={'students':std}
    print(ts)
    return render(request, 'index.html' , context=context)

# THERE ARE ALSO MANY METHODS TAHT NOT RETURN QUERY SET 