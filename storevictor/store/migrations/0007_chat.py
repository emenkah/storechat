# Generated by Django 3.2.8 on 2021-10-23 09:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211023_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=40, unique=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(default='pending', max_length=32)),
                ('payload', models.TextField(blank=True, null=True, verbose_name='Chat Payload')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client')),
                ('conversation_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.conversationparty')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.operator')),
            ],
        ),
    ]
