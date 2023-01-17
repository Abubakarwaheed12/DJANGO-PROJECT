from django.urls import path
from . import views


# view for home page   
urlpatterns = [
    path("" , views.set_session , name="home"), 
    path("get" , views.get_session , name="get"), 
    path("del" , views.del_session , name="get"), 
]