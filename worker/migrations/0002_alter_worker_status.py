# Generated by Django 4.2.2 on 2023-06-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=30),
        ),
    ]
