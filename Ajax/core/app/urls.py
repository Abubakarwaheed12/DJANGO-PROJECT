from django.urls import path
from app.views import home , savename
urlpatterns=[
    path('' , home , name='home'),
    path('saved' , savename , name='saved'),
]