# Generated by Django 3.0.5 on 2020-12-01 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shop',
        ),
    ]
