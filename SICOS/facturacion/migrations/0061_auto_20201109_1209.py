# Generated by Django 3.1 on 2020-11-09 17:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0060_auto_20201109_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 11, 9, 17, 9, 57, 4868, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 11, 9, 17, 9, 57, 4868, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='fac_especialista',
            name='fechafac_esp',
            field=models.DateField(default=datetime.datetime(2020, 11, 9, 17, 9, 57, 4868, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]
