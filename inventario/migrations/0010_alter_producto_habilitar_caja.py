# Generated by Django 4.1.7 on 2023-10-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_alter_producto_unidades_por_caja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='habilitar_caja',
            field=models.BooleanField(default=False),
        ),
    ]
