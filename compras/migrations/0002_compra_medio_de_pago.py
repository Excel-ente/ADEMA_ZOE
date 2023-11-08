# Generated by Django 4.1.7 on 2023-10-13 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='medio_de_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Cuenta Corriente', 'Cuenta Corriente')], default='Efectivo', max_length=25),
        ),
    ]
