# Generated by Django 3.1 on 2020-08-19 21:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='aporte_arl',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 21, 24, 59, 436930, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 21, 24, 59, 435931, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='fac_especialista',
            name='fechafac_esp',
            field=models.DateField(default=datetime.datetime(2020, 8, 19, 21, 24, 59, 439425, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]
