# Generated by Django 3.0.5 on 2020-04-28 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200428_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='beginning',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
