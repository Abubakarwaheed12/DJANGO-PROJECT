from django.contrib.auth.signals import user_logged_in , user_logged_out , user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in , sender=User)
def login_success(sender , request , user , **kwargs):
    print('-----------------------')
    print('Logged in signal ------------')
    print('sender : ' ,  sender)
    print('user : ' ,  user)
    print(f'kwargs  {kwargs}')
    
    
# user_logged_in.connect(login_success , sender=User)
# we can connect with decorator example on above 

# user logout signal 

@receiver(user_logged_out , sender=User)
def log_out(sender , request , user , **kwargs):
    print('-----------------------')
    print('Logged out signal ------------')
    print('sender : ' ,  sender)
    print('user : ' ,  user)
    print(f'kwargs  {kwargs}')
    
    
# user_logged_in.connect(login_success , sender=User)
# we can connect with decorator example on above 


# user logged in fail 

@receiver(user_login_failed , sender=User)
def log_out(sender , request , user , **kwargs):
    print('-----------------------')
    print('Logged in  Failed   signal ------------')
    print('sender : ' ,  sender)
    print('user : ' ,  user)
    print(f'kwargs  {kwargs}')
    
    
# user_logged_in.connect(login_success , sender=User)
# we can connect with decorator example on above 