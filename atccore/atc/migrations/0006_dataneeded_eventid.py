# Generated by Django 2.2.7 on 2020-01-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0005_auto_20191110_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataneeded',
            name='eventID',
            field=models.ManyToManyField(to='atc.EventID', verbose_name='Event ID(s)'),
        ),
    ]
