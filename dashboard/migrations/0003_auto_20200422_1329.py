# Generated by Django 3.0.5 on 2020-04-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200422_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='deadline',
            field=models.DateField(),
        ),
    ]
