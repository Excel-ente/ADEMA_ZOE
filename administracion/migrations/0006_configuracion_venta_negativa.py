# Generated by Django 4.1.7 on 2023-10-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_configuracion_v001'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='venta_negativa',
            field=models.BooleanField(default=True),
        ),
    ]