# Generated by Django 4.1.7 on 2023-10-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0013_alter_configuracion_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='ganancia_caja',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
