# Generated by Django 4.1.7 on 2023-10-13 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0004_alter_producto_codigo'),
        ('administracion', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=25)),
                ('precio', models.PositiveIntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
    ]