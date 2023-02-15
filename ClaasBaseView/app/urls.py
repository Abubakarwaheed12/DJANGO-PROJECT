from django.urls import path
from app.views import myView , home , HomeView  ,ContactForm

urlpatterns=[
    path('' , myView.as_view() , name='View'),
    path('home/' , home , name='home'),
    path('homeclass/' , HomeView.as_view() , name='homeclass'), 
    path('contact' , ContactForm.as_view() , name='contact'),
    ]