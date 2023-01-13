from django.shortcuts import render
from .forms import userreg
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=="POST":
        fm=userreg(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY')
        fm=userreg()    
    else:
        fm=userreg()
    return render(request , "home.html" , {'form':fm} )