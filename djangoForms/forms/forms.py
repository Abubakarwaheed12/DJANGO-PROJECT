from cProfile import label
import imp
from django import forms
from .models import user
class userregistration(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = user
        fields = ('name','email' , 'password',)
        labels={
            'name':'enter name',
            'email':'enter your email',
            }
