# Generated by Django 2.2.7 on 2019-11-10 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0004_auto_20191110_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detectionrule',
            old_name='dev_status',
            new_name='status',
        ),
    ]
