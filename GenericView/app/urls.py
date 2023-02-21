from django.urls import path
from app.views import myred

urlpatterns=[
    path('' , myred.as_view() , name='home'),
]