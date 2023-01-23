from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in , sender=User)
def loginsignal(sender , user, request , **kwargs):
    print('user logged in successfully now we can track user IP Address')
    ip = request.META.get('REMOTE_ADDR')
    print('ip is   :  ' , ip)
    request.session['ip']=ip