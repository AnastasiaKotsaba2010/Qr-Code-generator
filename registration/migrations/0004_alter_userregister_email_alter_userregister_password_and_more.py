# Generated by Django 5.1.5 on 2025-03-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_rename_user_userregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='username',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
