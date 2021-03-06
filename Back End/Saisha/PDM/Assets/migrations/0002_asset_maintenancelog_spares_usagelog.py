# Generated by Django 2.1.7 on 2019-02-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('FacilityName', models.CharField(max_length=250)),
                ('FactoryNum', models.CharField(max_length=250)),
                ('ProdlineNum', models.CharField(max_length=250)),
                ('MachineId', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stamp', models.DateTimeField()),
                ('Details', models.CharField(max_length=500)),
                ('Comments', models.CharField(max_length=1000)),
                ('MachineId', models.ForeignKey(on_delete=None, to='Assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Spares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComponentName', models.CharField(max_length=250)),
                ('Count', models.PositiveIntegerField()),
                ('MachineId', models.ForeignKey(on_delete=None, to='Assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='UsageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoursCount', models.PositiveIntegerField()),
                ('MachineId', models.ForeignKey(on_delete=None, to='Assets.Asset')),
            ],
        ),
    ]
