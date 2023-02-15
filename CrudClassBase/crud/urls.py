from django.urls import path
from crud import views
urlpatterns = [
    path('' , views.home),
    path('delete/<int:id>/' , views.delete , name='delete'),
    path('<int:id>' , views.update , name='update'),
]