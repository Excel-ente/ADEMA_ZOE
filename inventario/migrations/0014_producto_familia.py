# Generated by Django 4.1.7 on 2023-10-16 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0011_familia'),
        ('inventario', '0013_remove_producto_precio_mayorista'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.familia'),
        ),
    ]
