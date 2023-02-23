from django.urls import path
from app.views import profile
urlpatterns=[
    path('profile/' , profile , name='profile'),
]