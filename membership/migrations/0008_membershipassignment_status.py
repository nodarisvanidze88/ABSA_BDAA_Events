# Generated by Django 5.0.6 on 2024-09-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_alter_membershipassignment_member_delete_peoples'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipassignment',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]
