# Generated by Django 3.2.8 on 2021-10-23 09:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211023_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False, max_length=40, unique=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('resolved_datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('responding', 'Responding'), ('resolved', 'Resolved'), ('unresolved', 'Unresolved')], default='pending', max_length=32)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.client')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.operator')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
