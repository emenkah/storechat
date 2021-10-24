from django.contrib import admin
from .models import Store, Discount, Operator, Client, ConversationParty, ClientChat


# Register your models here.
admin.site.register(Store)
admin.site.register(Discount)
admin.site.register(Operator)
admin.site.register(Client)
admin.site.register(ConversationParty)
admin.site.register(ClientChat)

