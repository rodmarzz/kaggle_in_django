# Generated by Django 3.0.5 on 2020-05-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_dashboard_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='submission',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
