# Generated by Django 5.0.6 on 2024-06-17 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='submembershiptype',
            unique_together={('main_membership_type', 'sub_membership_type')},
        ),
    ]