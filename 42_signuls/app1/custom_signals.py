from django.dispatch import Signal,receiver

notification=Signal()

@receiver(notification)
def send_notification(sender,**kwargs):
    print("---------------------------")
    print("Notification")
    print("Sender",sender)
    print("Kwargs",kwargs)  