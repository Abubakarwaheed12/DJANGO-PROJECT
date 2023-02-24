from django.urls import path
from app.views import profile , clasbase_profile_view
#Impor Template View   
from django.views.generic.base import TemplateView
urlpatterns=[
    # path('profile/' , profile , name='profile'),
    path('p' , clasbase_profile_view.as_view(template_name='registration/profile.html')),
]