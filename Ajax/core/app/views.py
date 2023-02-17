from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
# Create your views here.

def home(request):
    
    return render(request, 'index.html')