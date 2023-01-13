import email
from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import user
from .forms import reg
from .models import user_form
# Create your views here.

def userdata(request):
    #  THE AUTO ID IS USED TO GENERATE THE ID FOR INPUT TAG  
    # AND THE LABEL_SUFFIX IS USED TO CONFIGURE THE LAbel
    # AND INITIAL VALUE AT RUNTIME 
    fm=user(auto_id='True' , label_suffix='......' , initial={'lname':'waheed','name':'abubakar', 'email':'AB@gmail.com', 'key':'snafkghdveshsb' , 'password':'acd'})
    # order fields 
    fm.order_fields(field_order=[ 'name', 'lname', 'email' ,])
    return render(request, 'user.html' ,{'form':fm},)

def thankyou(request):
    return render(request , 'success.html')

def register_user(request):
    if request.method == 'POST':
        fm=reg(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            re_password=fm.cleaned_data['re_password']
            agree=fm.cleaned_data['agree']
            # update karny k liye hamy user form k under ID dena parhy ga phir 
            # regs=user_form(id = 1 ,name=name , email=email , password=password)
            regs=user_form(name=name , email=email , password=password)
            
            regs.save()
            # DLETE KANRY K LIYE HAMY SIRF ID DENA PARTA HA 
            # regs.save(id=1)
            # print(name)
            # print(email)
            # print(password)
            # print(re_password)
            # print(agree)
            return HttpResponseRedirect('/user/success')
            # other way
            # return render(request , 'success.html' ,{'nm':name})
    else:
        fm=reg()
        print("ye get request sy aya ha ")
    return render(request, 'getform.html' , {'reg_form':fm})

