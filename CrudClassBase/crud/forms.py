from django import forms
from .models import user
from django.core import validators

class stureg(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = user
        fields = ('name','email', 'password',)