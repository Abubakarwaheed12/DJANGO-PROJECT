from django.urls import path
from crud import views
urlpatterns = [
    path('' , views.Home_View.as_view()),
    # path('' , views.home),
    path('delete/<int:id>/', views.deleteClass.as_view() , name='delete'),
    # path('delete/<int:id>/' , views.delete , name='delete'),
    path('<int:id>' , views.Updateclass.as_view() , name='update'),
    # path('<int:id>' , views.update , name='update'),
] 