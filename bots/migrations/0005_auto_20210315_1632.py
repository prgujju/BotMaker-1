# Generated by Django 3.1.4 on 2021-03-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0004_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender_tid',
            field=models.IntegerField(editable=False, help_text='Message sender tid'),
        ),
    ]
