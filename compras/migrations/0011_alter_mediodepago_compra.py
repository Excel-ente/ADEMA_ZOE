# Generated by Django 4.1.7 on 2023-10-15 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0010_remove_compra_medio_de_pago_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediodepago',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medios_de_pago', to='compras.compra'),
        ),
    ]
