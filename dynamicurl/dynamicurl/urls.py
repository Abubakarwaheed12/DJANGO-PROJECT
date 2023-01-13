
from django.contrib import admin
from django.urls import path , include
from dynamic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home , name='home'),
    path('', include('dynamic.urls'))
    
]
