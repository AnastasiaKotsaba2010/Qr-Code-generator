# Generated by Django 5.1.5 on 2025-03-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_rename_registration_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserRegister',
        ),
    ]
