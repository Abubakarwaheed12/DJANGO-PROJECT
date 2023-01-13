from django.urls import path
from showdata import views
urlpatterns=[
    path('student/' , views.studentinfo),
]