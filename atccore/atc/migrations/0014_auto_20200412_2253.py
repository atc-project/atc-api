# Generated by Django 2.2.7 on 2020-04-12 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atc', '0013_auto_20200412_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseplaybook',
            name='tags',
            field=models.ManyToManyField(to='atc.Tag', verbose_name='Tag(s)'),
        ),
    ]
