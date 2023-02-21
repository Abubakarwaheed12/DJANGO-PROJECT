from django.shortcuts import render
from django.views.generic.edit import FormView , CreateView
from django.views.generic import TemplateView
from app.models import ContactForm
from app.forms import  Contact 
# Create your views here.

class ContactView(FormView): 
    template_name='app/index.html'
    form_class=Contact
    success_url='thankyou'
    
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['message'])

        return super().form_valid(form)
class ThankYou(TemplateView):
    template_name='app/thankyou.html'
      

# Create View 