# Generated by Django 2.1.7 on 2019-02-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaintenanceLog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancelog',
            name='Name',
            field=models.CharField(default='', max_length=260),
        ),
    ]
