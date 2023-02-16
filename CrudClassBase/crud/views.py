import email
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import render , HttpResponseRedirect
from .forms import stureg
from .models import user
from django.views.generic.base import TemplateView , RedirectView
from django.views import View
# Create your views here.
# All Views Changed to Class Base View 
# Class Base View 
class Home_View(TemplateView):
    template_name='home.html'

    def get_context_data(self ,*args , **kwargs):
        context=super().get_context_data(**kwargs)
         
        fm=stureg
        stud=user.objects.all()
        context={'form':fm , 'stu':stud}
        return context
    
    def post(self, request):
        fm=stureg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=user(name=nm , email=em , password=ps)
            reg.save()
            fm=stureg()
            return HttpResponseRedirect('/')

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

# Delete Class View 
class deleteClass(RedirectView):
    url='/'
    def get_redirect_url(self , *args , **kwargs):
        del_id=kwargs['id']
        user.objects.get(pk=del_id).delete()        
        return super().get_redirect_url(*args)
    
    
    
# for del
# def delete(request , id):
    # if request.method=="POST":
        # pi=user.objects.get(pk=id)
        # pi.delete()
    # return HttpResponseRedirect('/') 

# Update Class View
class Updateclass(View):
    def get(self , request , id):
        pi=user.objects.get(pk=id)
        fm=stureg(instance=pi)        
        return render(request , 'update.html' , {'id':id, "form":fm})
    
    def post(self , request , id):
        pi=user.objects.get(pk=id)
        fm=stureg(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  
    
# update data 
# def update(request , id):
#     if request.method=="POST":
#         pi=user.objects.get(pk=id)
#         fm=stureg(request.POST , instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')  
            
#     else:
#         pi=user.objects.get(pk=id)
#         fm=stureg(instance=pi)
#     return render(request , 'update.html' , {'id':id, "form":fm})
    

