# Generated by Django 3.2.8 on 2021-10-24 06:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_rename_chat_clientchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperatorChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=40, unique=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(default='pending', max_length=32)),
                ('sending_message', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Please ensure that you use right characters in your message', regex='[\\*a-zA-Z0-9_\\-\\.\\{\\}]*$')], verbose_name='Chat Payload')),
                ('is_deleted', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.clientchat', to_field='uuid')),
                ('conversation_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.conversationparty', to_field='uuid')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.operator', to_field='uuid')),
            ],
        ),
    ]
