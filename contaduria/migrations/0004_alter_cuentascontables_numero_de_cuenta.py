# Generated by Django 4.1.7 on 2023-10-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contaduria', '0003_alter_cuentascontables_numero_de_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentascontables',
            name='numero_de_cuenta',
            field=models.IntegerField(unique=True),
        ),
    ]
