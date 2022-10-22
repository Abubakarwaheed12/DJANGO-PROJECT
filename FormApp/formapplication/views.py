from django.shortcuts import render
from django.http import HttpResponse

from .forms import user 
# Create your views here.

def userdata(request):
    #  THE AUTO ID IS USED TO GENERATE THE ID FOR INPUT TAG  
    # AND THE LABEL_SUFFIX IS USED TO CONFIGURE THE LAbel
    # AND INITIAL VALUE AT RUNTIME 
    fm=user(auto_id='True' , label_suffix='......' , initial={'lname':'waheed','name':'abubakar', 'email':'AB@gmail.com', 'key':'snafkghdveshsb' , 'password':'acd'})
    # order fields 
    fm.order_fields(field_order=[ 'name', 'lname', 'email' ,])
    return render(request, 'user.html' ,{'form':fm},)