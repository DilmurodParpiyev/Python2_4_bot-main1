# Generated by Django 4.2.4 on 2024-01-09 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0014_rename_tur_maxsulotlar_turi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='korzinka',
            old_name='turi',
            new_name='tur',
        ),
        migrations.RenameField(
            model_name='maxsulotlar',
            old_name='turi',
            new_name='tur',
        ),
    ]
