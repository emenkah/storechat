# Generated by Django 3.2.8 on 2021-10-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_chat_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='communication',
            field=models.CharField(blank=True, choices=[('sending', 'sending'), ('receiving', 'receiving')], max_length=12, null=True),
        ),
    ]
