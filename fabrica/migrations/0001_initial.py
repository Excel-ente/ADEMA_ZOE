# Generated by Django 4.1.7 on 2023-10-18 03:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0014_producto_familia'),
        ('administracion', '0015_configuracion_venta_por_caja'),
    ]

    operations = [
        migrations.CreateModel(
            name='gastosAdicionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=120)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('unidad_medida', models.CharField(choices=[('Unidades', 'Unidades'), ('Kilogramos', 'Kilogramos'), ('Litros', 'Litros'), ('Onzas', 'Onzas'), ('Libras', 'Libras')], default='Unidades', max_length=10)),
                ('costo', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('ultima_actualizacion', models.DateField(default=datetime.date.today)),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.proveedor')),
            ],
            options={
                'verbose_name': 'ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porciones', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('fecha_de_actualizacion', models.DateField(auto_now_add=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
            options={
                'verbose_name': 'receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='ingredientereceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad_de_medida', models.CharField(choices=[('Unidades', 'Unidades'), ('Gramos', 'Gramos'), ('Mililitros', 'Mililitros'), ('Onzas', 'Onzas'), ('Libras', 'Libras')], default='Unidades', max_length=10)),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, max_digits=20)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.ingrediente')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.receta')),
            ],
            options={
                'verbose_name': 'ingrediente',
                'verbose_name_plural': 'Productos incluidos en la receta',
            },
        ),
        migrations.CreateModel(
            name='adicionalreceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('adicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.gastosadicionales')),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabrica.receta')),
            ],
        ),
    ]