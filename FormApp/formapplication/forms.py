import email
from pickle import TRUE
from wsgiref.validate import validator
from django import forms
from django.core import validators
class user(forms.Form):
    # FORM FIELD ARGUMENTS 
    name=forms.CharField(label='enter name', label_suffix='', initial='jutt' , 
    error_messages={'required':'name not enter'} ,)
    lname=forms.CharField()
    email=forms.EmailField()
    # hiidden 
    key=forms.CharField(widget=forms.HiddenInput())
    
    # BUILT IN WIDGETS examples
    # DateInput
    # textInput
    
    # PasswordInput
    password=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form',
    }))
    
    
#CLASS FOR OTHER FORM 
class reg(forms.Form):
    
    name=forms.CharField()
    email=forms.EmailField(label='enter email',)
    password=forms.CharField(widget=forms.PasswordInput , required=TRUE)
    re_password=forms.CharField(widget=forms.PasswordInput , required=True)
    agree=forms.BooleanField(label='I AGREE')
    # Validate Complete FORM AT-ONCE 
    # THEY RETURNED CLEANED DATA 
    
    def clean(self):
        cleaned_data= super().clean()
        pas=cleaned_data['password']
        rpas=cleaned_data['re_password']
        if pas != rpas : 
            raise forms.ValidationError("password not match")  
    
    # Other Way To clean data 
    # CLAEN SPECIIC FIELD 
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname) < 4 :
    #         raise forms.ValidationError("enter name greater than 4 ")
    #     return valname
    
