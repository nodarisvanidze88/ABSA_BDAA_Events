# Generated by Django 5.0.6 on 2024-06-16 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipassignment',
            name='acceptance',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 6, 16, 20, 18, 58, 511833, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='membershipassignment',
            name='paid_till',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 6, 16, 20, 18, 58, 511851, tzinfo=datetime.timezone.utc)),
        ),
    ]
