from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

# Template View
class HomeTemplate(TemplateView):
    template_name='index.html' 
    
    
    def get_context_data(self , **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='abu bakar waheed'
        
        return context
    
# Redirect View 