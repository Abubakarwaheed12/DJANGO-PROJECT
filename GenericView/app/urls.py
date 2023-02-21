from django.urls import path
from app.views import myred , mydetailview

urlpatterns=[
    path('' , myred.as_view() , name='home'),
    path('<int:pk>' , mydetailview.as_view(), name='detail'),
]