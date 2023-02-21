from django.urls import path
from app.views import HomeTemplate , RedirectViewMy
urlpatterns=[
     path('' , HomeTemplate .as_view() , name='home'),
     path('google' ,RedirectViewMy.as_view(),)
    #  we can also pass pattern name in redirect view the pattern name is name of url of any url link 
]