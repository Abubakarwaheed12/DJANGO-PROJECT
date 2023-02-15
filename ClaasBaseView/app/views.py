from django.shortcuts import render , HttpResponse , redirect
from django.views import View
# Create your views here.
# Function Base View 
def myview(request):
    return HttpResponse('hi this is function base View ')

#  Class Base View
class myView(View):
    
    def get(self, request):
        return HttpResponse('Hi this is Class Base')


# Render Page Through Class And Function Base 
def home(request):
    return render(request, 'index.html')


class HomeView(View):
    name='Abu Bakar'
    def get(self , request , **kwargs):
        
        context={
            'name':self.name,
        }
        return render(request, 'index.html' , context)
  
  
# Contact form in class based View 
class ContactForm(View):
    def get(self ,  request):
        return render(request, 'contact.html')
    
    
    def post(self , request):
        name=request.POST.get('name')
        print(name)
        
        # return HttpResponse('Your form Data recieved Successfully')
        return redirect('View')