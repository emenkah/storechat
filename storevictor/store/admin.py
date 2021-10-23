from django.contrib import admin
from .models import Store, Operator, Client, ConversationParty, Chat


# Register your models here.
admin.site.register(Store)
admin.site.register(Operator)
admin.site.register(Client)
admin.site.register(ConversationParty)
admin.site.register(Chat)

