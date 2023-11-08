# Generated by Django 4.1.7 on 2023-11-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='costo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=25, null=True, verbose_name='Costo unit.'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25, verbose_name='Precio Pesos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_usd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25, verbose_name='Precio Dolares'),
        ),
    ]
