from django.urls import path
from . import views


# view for home page   
urlpatterns = [
    path("" , views.home , name="home") , 
]