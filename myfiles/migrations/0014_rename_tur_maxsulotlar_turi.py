# Generated by Django 4.2.4 on 2024-01-09 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0013_rename_turi_maxsulotlar_tur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maxsulotlar',
            old_name='tur',
            new_name='turi',
        ),
    ]