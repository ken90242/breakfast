# Generated by Django 3.0.5 on 2020-12-01 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
