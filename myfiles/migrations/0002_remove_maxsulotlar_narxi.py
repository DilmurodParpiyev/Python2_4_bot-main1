# Generated by Django 4.2.4 on 2023-11-07 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maxsulotlar',
            name='narxi',
        ),
    ]