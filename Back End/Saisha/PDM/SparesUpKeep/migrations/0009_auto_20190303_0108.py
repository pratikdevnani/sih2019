# Generated by Django 2.1.7 on 2019-03-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SparesUpKeep', '0008_auto_20190303_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]