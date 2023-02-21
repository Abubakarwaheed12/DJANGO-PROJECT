from django.shortcuts import render
from django.views.generic.edit import FormView , CreateView, DeleteView , UpdateView
from django.views.generic import TemplateView
from app.models import ContactForm
from app.forms import  Contact 
from django import forms 
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
# This Three Line Of codes will work to  create data in tables 
class ContactCreateView(CreateView):
    model=ContactForm
    fields=['name', 'message']
    label=['']
    success_url='thankyou'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Enter Name..'})
        form.fields['message'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Message / Qoute'})
        return form
 
#  The Same Way For Creatr Update and Delete View

class MyUpdateView(UpdateView):
    model=ContactForm
    fields=['name' , 'message']
    success_url='/thankyou'
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Enter Name..'})
        form.fields['message'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Message / Qoute'})
        return form

# Delete View 
class MydelView(DeleteView):
    model=ContactForm
    success_url='/thankyou'
    
    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Enter Name..'})
        form.fields['message'].widget=forms.TextInput(attrs={'class':'mycl','placeholder': 'Message / Qoute'})
        return form