# Generated by Django 4.1.7 on 2023-10-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporteventas',
            name='fecha',
            field=models.DateField(),
        ),
    ]
