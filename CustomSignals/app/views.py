from django.shortcuts import render
from app import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None , request=request , user=['abu' , 'bakar'])
    return render(request, 'index.html')