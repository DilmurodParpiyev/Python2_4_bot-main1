# Generated by Django 4.2.4 on 2023-11-08 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0011_alter_maxsulotlar_turi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maxsulotlar',
            name='turi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.menu'),
        ),
    ]
