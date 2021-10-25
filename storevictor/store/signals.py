from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OperatorChat, Schedule
import datetime

@receiver(post_save, sender=OperatorChat)
def create_profile(sender, instance, created, **kwargs):
    if created:
        timezone_of_client = instance.conversation_party.client.timezone

        now = datetime.datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        datetime_format = "%Y-%m-%d %H:%M:%S"
        low_ref_datetime_string = date_string + " " + "09:00:00"
        upper_ref_datetime_string = date_string + " " + "17:00:00"
        low_ref_datetime_object = datetime.datetime.strptime(low_ref_datetime_string, datetime_format)
        upper_ref_datetime_object = datetime.datetime.strptime(upper_ref_datetime_string, datetime_format)

        last_entry = Schedule.objects.filter(sending_datetime__gte=datetime.datetime.now()).order_by('sending_datetime').last()
        
        interval = (60.0/90.0) * 60.0
        
        if not last_entry:
            sending_datetime = datetime.datetime.now()
        else:   
            sending_datetime = last_entry + datetime.timedelta(seconds=interval)
        
        if sending_datetime < low_ref_datetime_object or sending_datetime > upper_ref_datetime_object:
            sending_datetime = low_ref_datetime_object + datetime.timedelta(days=1)
        
        
        Schedule.objects.create(chat = instance, sending_datetime=sending_datetime)
