# Generated by Django 3.0.5 on 2020-04-26 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200426_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='beginning',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 21, 1, 2, 127237, tzinfo=utc)),
        ),
    ]
