# Generated by Django 5.1.7 on 2025-03-08 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number_field',
            new_name='phone_number',
        ),
    ]
