# Generated by Django 2.2.1 on 2019-05-25 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190524_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='qr_code',
        ),
    ]
