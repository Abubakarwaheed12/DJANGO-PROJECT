from django.urls import path
from app.views import HomeTemplate
urlpatterns=[
     path('' , HomeTemplate .as_view() , name='home'),
]