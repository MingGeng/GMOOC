# Generated by Django 2.0.2 on 2018-03-12 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='messaage',
            new_name='message',
        ),
    ]