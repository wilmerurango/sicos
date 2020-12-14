# Generated by Django 3.1 on 2020-10-02 14:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0011_auto_20201001_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 14, 36, 59, 78467, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 14, 36, 59, 78467, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='fac_especialista',
            name='fechafac_esp',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 14, 36, 59, 81488, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]
