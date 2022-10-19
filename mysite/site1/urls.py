from django.urls import path
from site1 import views

urlpatterns=[
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services ,name='ab'),
    path('dynamic/', views.dynamic),
]