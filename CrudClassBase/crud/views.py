import email
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render , HttpResponseRedirect
from .forms import stureg
from .models import user
from django.views.generic.base import TemplateView
# Create your views here.

# Class Base View 
class Home_View(TemplateView):
    template_name='home.html'

    def get_context_data(self ,*args , **kwargs):
        context=super().get_context_data(**kwargs)
         
        fm=stureg
        stud=user.objects.all()
        context={'form':fm , 'stu':stud}
        return context

# Function Base View 
# def home(request):
    # if request.method=='POST':
        # fm=stureg(request.POST)
        # if fm.is_valid():
            # nm=fm.cleaned_data['name']
            # em=fm.cleaned_data['email']
            # ps=fm.cleaned_data['password']
            # reg=user(name=nm , email=em , password=ps)
            # reg.save()
            # fm=stureg()
        # 
    # else:
        # fm=stureg
    # stud=user.objects.all()
    # return render (request , 'home.html', {'form':fm , 'stu':stud})

# for del
def delete(request , id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

# update data 
def update(request , id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        fm=stureg(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
            
    else:
        pi=user.objects.get(pk=id)
        fm=stureg(instance=pi)
    return render(request , 'update.html' , {'id':id, "form":fm})
    

