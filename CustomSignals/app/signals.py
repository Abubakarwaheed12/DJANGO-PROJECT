from django.dispatch import Signal , receiver
#  creating custom signal 
notification=Signal(providing_args=['sender' , 'user'])

@receiver(notification)
def show_notification(sender , **kwargs):
    print(sender)
    print(f'{kwargs}')
    print('My Custom Notifications')