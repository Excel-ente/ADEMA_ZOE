# Generated by Django 4.1.7 on 2023-10-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_rename_ganancia_unitaria_configuracion_ganancia_mayorista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='v001',
            field=models.BooleanField(default=True),
        ),
    ]
