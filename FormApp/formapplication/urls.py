from django.urls import path
from . import views
urlpatterns = [
    path('user' , views.userdata),
    path('reg/' , views.register_user),
    path('success/' , views.thankyou),
]
