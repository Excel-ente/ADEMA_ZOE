# Generated by Django 4.1.7 on 2023-10-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0006_rename_total_iva_reporteventas_total_iva_10_5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporteventas',
            name='total_cuenta_corriente',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='reporteventas',
            name='total_efectivo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='reporteventas',
            name='total_redondeo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='reporteventas',
            name='total_transferencia',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
    ]