# Generated by Django 5.0.7 on 2024-08-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderField',
            new_name='OrderItem',
        ),
    ]
