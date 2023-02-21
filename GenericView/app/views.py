from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from app.models import patient
# Create your views here.

class myred(ListView):
    model=patient
    print(model)
    
    # We can filter data in class base list view
    
    def get_queryset(self):
        return patient.objects.filter(age='17')
    
    def get_context_data(self , *args , **kwargs):
        context=super().get_context_data(  *args , **kwargs)
        if self.request.COOKIES['user']=='abu bakar':
            context['user']='this is abu bakar'
        else:
            context['user']='this is not abu bakar'    
        
        return context
    

# Detail class based view 
class mydetailview(DetailView):
    model = patient
    context_object_name='patient'
    # if we want to use our custom template for showing the data
    # template_name='patient'
    
    def get_context_data(self , **jwargs):
        context=super().get_context_data(**jwargs)
        
        return context