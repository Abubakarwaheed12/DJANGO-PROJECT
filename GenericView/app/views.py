from django.shortcuts import render
from django.views.generic.list import ListView
from app.models import patient
# Create your views here.

class myred(ListView):
    model=patient
    print(model)