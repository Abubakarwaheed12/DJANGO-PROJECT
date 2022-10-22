import email
from django import forms

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