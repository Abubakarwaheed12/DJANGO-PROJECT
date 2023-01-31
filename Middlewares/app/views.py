from django.shortcuts import render

# Create your views here.

def home(request):
    print('I am View')
    return render(request, 'home.html')