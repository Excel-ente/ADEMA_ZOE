# Generated by Django 4.1.7 on 2023-10-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_compra_total_pagado_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total_pagado_2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=25, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='total_pagado_3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=25, null=True),
        ),
    ]
