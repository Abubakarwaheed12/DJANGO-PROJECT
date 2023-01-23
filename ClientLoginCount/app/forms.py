from dataclasses import fields
import email
from pyexpat import model
from telnetlib import AUTHENTICATION


# form with django full AUTHENTICATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm

class sign_up(UserCreationForm):
    class Meta:
        model=User
        fields=['username' ,'first_name' , 'last_name' , 'email',]
        
    def __init__(self, *args, **kwargs):
        super(sign_up,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Username'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Password Confirmation'})       
    
    
# edit user profie form 
class editprofileform(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields=['username' , 'first_name','last_name', 'email','date_joined','last_login']


#edit Admin Profile 
class editadminprofileform(UserChangeForm):
    password=None
    
    class Meta:
        model=User
        fields='__all__'
        