from cProfile import label
import imp
from django import forms
from .models import user
class userregistration(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""
        model = user
        # selecting model form fields in django 
        fields = ('name','email' , 'password',)
        # all
        # fields='__all__'
        # other method is to exclude 
        # exclude=['name']
        labels={
            'name':'enter name',
            'email':'enter your email',
            'password':'enter password',
            }

# model form inheritence 
class teacherreg(userregistration):
    class Meta(userregistration.Meta):
        fields=['teacher_name','email','password']