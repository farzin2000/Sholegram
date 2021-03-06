# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(default='safd', null=True, upload_to='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=400)),
                ('time', models.TimeField(auto_now=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupAssignment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Group')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupRequest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField(auto_now=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Group')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authsystem.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessageSeen',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('membershipId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.UserGroupAssignment')),
                ('messageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Message')),
            ],
        ),
    ]
