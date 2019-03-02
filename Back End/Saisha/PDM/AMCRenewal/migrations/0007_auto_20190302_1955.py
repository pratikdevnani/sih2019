# Generated by Django 2.1.7 on 2019-03-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMCRenewal', '0006_auto_20190302_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amc',
            old_name='Category',
            new_name='Factory',
        ),
        migrations.RemoveField(
            model_name='amc',
            name='FactoryID',
        ),
        migrations.RemoveField(
            model_name='amc',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='amc',
            name='ProductionLine',
            field=models.CharField(default='', max_length=250, null=True),
        ),
    ]