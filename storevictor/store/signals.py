from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OperatorChat, Schedule


@receiver(post_save, sender=OperatorChat)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Schedule.objects.create(chat = instance)
