# Generated by Django 5.0.6 on 2024-06-16 20:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershiptType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=10)),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(blank=True, max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('dateOfBirth', models.DateField(blank=True)),
                ('defaultEmail', models.EmailField(max_length=254)),
                ('secondaryEmail', models.EmailField(blank=True, max_length=254)),
                ('optionalEmail', models.EmailField(blank=True, max_length=254)),
                ('defaultChapter', models.CharField(blank=True, max_length=50)),
                ('secondaryChapter', models.CharField(blank=True, max_length=50)),
                ('optionalChapter', models.CharField(blank=True, max_length=50)),
                ('defaultState', models.CharField(blank=True, max_length=50)),
                ('secondaryState', models.CharField(blank=True, max_length=50)),
                ('optionalState', models.CharField(blank=True, max_length=50)),
                ('businessName', models.CharField(blank=True, max_length=200)),
                ('phoneHome', models.CharField(blank=True, max_length=100)),
                ('phoneWork', models.CharField(blank=True, max_length=100)),
                ('phoneMobile', models.CharField(blank=True, max_length=100)),
                ('phoneFax', models.CharField(blank=True, max_length=100)),
                ('defaultAddress', models.CharField(blank=True, max_length=300)),
                ('secondaryAddress', models.CharField(blank=True, max_length=300)),
                ('optionalAddress', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SubMembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submembershiptype', models.CharField(max_length=50)),
                ('mainMembershipType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainMembership', to='membership.membershiptype')),
            ],
        ),
        migrations.CreateModel(
            name='MembershipAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceptance', models.DateField(blank=True, default=datetime.datetime(2024, 6, 16, 20, 17, 38, 287900))),
                ('paid_till', models.DateField(blank=True, default=datetime.datetime(2025, 6, 16, 20, 17, 38, 287914))),
                ('membershipType', models.ManyToManyField(to='membership.membershiptype')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='membership.peoples')),
                ('submembershipType', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='membership.submembershiptype')),
            ],
        ),
    ]
