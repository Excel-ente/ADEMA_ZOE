# Generated by Django 4.1.7 on 2023-11-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_compraproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraproducto',
            name='Costo',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
        ),
    ]