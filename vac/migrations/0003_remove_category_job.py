# Generated by Django 3.2.6 on 2021-08-16 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0002_category_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='job',
        ),
    ]
