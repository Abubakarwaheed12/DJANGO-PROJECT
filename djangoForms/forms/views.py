import email
from unicodedata import name
from django.shortcuts import render
from .forms import userregistration 
from .forms import teacherreg
from .models import user
# Create your views here.

def userview(request):
    if request.method=='POST':
        fm =userregistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            print(nm)
            print(em)
            print(ps)
            # for saving data in database 
            # sv=user(name=nm , email=em , password=ps)
            # sv.save()
    else:
        fm=userregistration()
        th=teacherreg()
    return render(request , 'form.html' , {'form':fm , "th":th})