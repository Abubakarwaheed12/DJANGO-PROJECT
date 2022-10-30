from socket import fromshare
from django import forms
from .models import user

class userreg(forms.ModelForm):
    class Meta:
        model = user
        fields = ('id','name','email','password')

    