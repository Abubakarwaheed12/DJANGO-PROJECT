from django.urls import path
from . import views

urlpatterns = [
    path('student/<my_id>/' , views.student , name='student')
]