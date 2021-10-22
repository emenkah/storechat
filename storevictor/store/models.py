from django.db import models
from django.contrib.auth import get_user_model
from utility.validators import no_past, PossiblePhoneNumberField
import uuid
import pytz

# Create your models here.
User = get_user_model()

class Store(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    
   
    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    name = models.CharField('Store Name', max_length=256, unique=True, blank=True, null=True )
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    telephone =  PossiblePhoneNumberField("Telephone No.", unique=True)
    created_by = models.ForeignKey(User, to_field='uuid', on_delete=models.CASCADE, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
