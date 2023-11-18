# Generated by Django 2.2.7 on 2019-11-22 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191122_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='address',
            field=models.CharField(default='HealthPlus, Rohini-22, New Delhi', max_length=100),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 22, 15, 38, 3, 754406)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2019, 11, 22, 15, 38, 3, 754406)),
        ),
    ]