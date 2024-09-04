# Generated by Django 5.0.6 on 2024-09-04 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_alter_membershipassignment_sub_membership_type'),
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipassignment',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='peoples.peoples'),
        ),
        migrations.DeleteModel(
            name='Peoples',
        ),
    ]