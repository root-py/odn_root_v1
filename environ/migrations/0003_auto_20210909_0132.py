# Generated by Django 3.2.7 on 2021-09-09 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('environ', '0002_environ_buoy_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='environ',
            old_name='x',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='environ',
            old_name='y',
            new_name='lon',
        ),
    ]
