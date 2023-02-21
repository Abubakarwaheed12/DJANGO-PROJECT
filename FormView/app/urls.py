from django.urls import path
from app.views import ContactView , ThankYou
urlpatterns=[
    path('', ContactView.as_view() , name='contact'),
    path('thankyou' , ThankYou.as_view() , name='thankyou' ),
]