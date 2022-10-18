from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# we can create multiple views in single application
def index(request):
    return HttpResponse('HOME PAGE HERE ........')

def ab(request):
    a='<h1>abu bakar</h1>'
    return HttpResponse(a)

def learnpy(request):
    return HttpResponse('<b>Learn Django</b>')