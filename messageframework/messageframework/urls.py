from django.contrib import admin
from django.urls import path
from message import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', views.home),
]
