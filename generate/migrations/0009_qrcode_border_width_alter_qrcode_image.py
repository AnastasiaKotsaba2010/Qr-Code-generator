# Generated by Django 5.1.5 on 2025-03-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate', '0008_remove_qrcode_border'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='border_width',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
