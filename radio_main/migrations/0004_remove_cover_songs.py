# Generated by Django 3.0.7 on 2020-07-24 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio_main', '0003_auto_20200724_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cover',
            name='songs',
        ),
    ]
