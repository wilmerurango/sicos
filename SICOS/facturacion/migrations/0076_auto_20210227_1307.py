# Generated by Django 3.1 on 2021-02-27 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0075_auto_20210227_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 2, 27, 18, 7, 7, 272861, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2021, 2, 27, 18, 7, 7, 272861, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='fac_especialista',
            name='fechafac_esp',
            field=models.DateField(default=datetime.datetime(2021, 2, 27, 18, 7, 7, 275852, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]