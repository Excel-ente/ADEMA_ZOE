# Generated by Django 4.1.7 on 2023-11-08 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0006_mediodepago'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'venta', 'verbose_name_plural': 'Ventas'},
        ),
    ]