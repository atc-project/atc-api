# Generated by Django 2.2.7 on 2020-04-12 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0012_auto_20200412_2235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='responseplaybook',
            old_name='tag',
            new_name='tags',
        ),
    ]
