# Generated by Django 3.0.5 on 2020-05-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_remove_dashboard_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='test',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
