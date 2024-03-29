from django import forms


# Create your models here.

class Contact(forms.Form):
    name=forms.CharField(max_length=200)
    message=forms.CharField(max_length=2112)
    
    
    def __str__(self):
        return f'{self.name} ({self.message}) '
    
    
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for key, field in self.fields.items():
          field.label = ""