from django.urls import path
from . import views


# view for home page   
urlpatterns = [
    path("" , views.setcook , name="home"), 
    path("get" , views.getcook , name="get"), 
    path("del" , views.delcook , name="get"), 
]