# Generated by Django 4.0.3 on 2022-05-16 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_state_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='State',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
