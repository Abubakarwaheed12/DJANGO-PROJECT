# URLS INSIDE THE APPLICATION
from django.urls import path  
from myapp import views

urlpatterns=[
    path('hello/', views.ab),
    path('py/', views.learnpy),
]