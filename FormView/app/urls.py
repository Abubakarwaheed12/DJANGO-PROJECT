from django.urls import path
from app.views import ContactView , ThankYou , ContactCreateView
urlpatterns=[
    path('', ContactView.as_view() , name='contact'),
    path('thankyou' , ThankYou.as_view() , name='thankyou' ),
    path('contact', ContactCreateView.as_view() , name='contactCrateByUs'),
]