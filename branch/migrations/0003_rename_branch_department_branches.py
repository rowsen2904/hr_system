# Generated by Django 4.2.2 on 2023-06-24 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_alter_branch_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='branch',
            new_name='branches',
        ),
    ]
