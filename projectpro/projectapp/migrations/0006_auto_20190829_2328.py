# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-29 17:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactData',
        ),
    ]
