# Generated by Django 3.2.8 on 2021-10-24 06:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0014_alter_chat_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat',
            new_name='ClientChat',
        ),
    ]
