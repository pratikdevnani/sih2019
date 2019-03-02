# Generated by Django 2.1.7 on 2019-02-27 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMCRenewal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amc',
            old_name='machineID',
            new_name='MachineID',
        ),
        migrations.RemoveField(
            model_name='amc',
            name='supplier',
        ),
        migrations.AddField(
            model_name='amc',
            name='AMCCompany',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='amc',
            name='Category',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='amc',
            name='Company',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='amc',
            name='ExpiryDate',
            field=models.DateField(default=datetime.date(2019, 2, 27)),
        ),
        migrations.AddField(
            model_name='amc',
            name='FactoryID',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='amc',
            name='Quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
