# Generated by Django 3.0.7 on 2020-07-08 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
    ]