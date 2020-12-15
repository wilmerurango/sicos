# Generated by Django 3.1 on 2020-12-15 14:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0065_auto_20201215_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro_actividad',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='facturacion.especialista', verbose_name='Especialista'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 12, 15, 14, 21, 48, 997573, tzinfo=utc), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='fechafact_esp',
            field=models.DateField(default=datetime.datetime(2020, 12, 15, 14, 21, 48, 997573, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
        migrations.AlterField(
            model_name='fac_especialista',
            name='fechafac_esp',
            field=models.DateField(default=datetime.datetime(2020, 12, 15, 14, 21, 48, 997573, tzinfo=utc), verbose_name='Fecha de Registro'),
        ),
    ]