from django.db import models
from django.contrib.auth import get_user_model
from utility.validators import no_past, PossiblePhoneNumberField
from utility.models import Address
import uuid
import pytz

# Create your models here.
User = get_user_model()
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Store(models.Model):

    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    name = models.CharField('Store Name', max_length=256, unique=True, blank=True, null=True )
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    telephone =  PossiblePhoneNumberField("Telephone No.", unique=True)
    created_by = models.ForeignKey(User, to_field='uuid', on_delete=models.CASCADE, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.timezone)


class Client(models.Model):
    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    user = models.ForeignKey(User, to_field="uuid", on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    address = models.ManyToManyField(Address, blank=True, null=True)
    #telephone =  PossiblePhoneNumberField("Telephone No.", unique=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.user, self.timezone)


class Operator(models.Model):

    DEPT_CHOICE = (
        ('sales', 'sales'),
        ('grocery', 'Grocery'),
        ('pharmacy', 'Pharmacy'),
        ('operations', 'Operations'),
    )

    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field="uuid", on_delete=models.CASCADE)
    department = models.CharField(max_length=32, choices=DEPT_CHOICE, default='operations')
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '{}-{}-{}'.format(self.user, self.store, self.department)


class ConversationParty(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('responding', 'Responding'),
        ('resolved', 'Resolved'),
        ('unresolved', 'Unresolved'),
        
        
    )
    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    store = models.ForeignKey(Store, to_field="uuid", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, to_field="uuid", on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, to_field="uuid", on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    resolved_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICE, default='pending')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{}-{}'.format(self.store, self.client)

class Chat(models.Model):
    uuid = models.CharField(default=uuid.uuid4, max_length=40, editable=False, unique=True)
    conversation_party = models.ForeignKey(ConversationParty, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=32,  default='pending')
    payload = models.TextField('Chat Payload',blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.store, self.conversation_party.uuid)

class Schedule(models.Model):
    pass
