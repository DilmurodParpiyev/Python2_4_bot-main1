# Generated by Django 4.2.4 on 2023-11-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0006_delete_korzinka_delete_subscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maxsulotlar',
            name='turi',
        ),
    ]
