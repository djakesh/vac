# Generated by Django 3.2.6 on 2021-08-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0004_category_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='description',
        ),
    ]