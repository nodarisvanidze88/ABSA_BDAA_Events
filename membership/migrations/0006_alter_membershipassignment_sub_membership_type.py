# Generated by Django 5.0.6 on 2024-06-22 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_alter_membershipassignment_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipassignment',
            name='sub_membership_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='membership.submembershiptype'),
        ),
    ]