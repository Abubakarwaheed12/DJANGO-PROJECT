from django.urls import path
from app.views import ContactView , ThankYou , ContactCreateView , MyUpdateView ,MydelView
urlpatterns=[
    path('', ContactView.as_view() , name='contact'),
    path('thankyou' , ThankYou.as_view() , name='thankyou' ),
    path('contact', ContactCreateView.as_view() , name='contactCrateByUs'),
    path('update/<int:pk>', MyUpdateView.as_view() , name='update'),
    path('delete/<int:pk>', MydelView.as_view() , name='delete'),
]