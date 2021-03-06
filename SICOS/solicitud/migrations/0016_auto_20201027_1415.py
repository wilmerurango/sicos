# Generated by Django 3.1 on 2020-10-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0015_auto_20201027_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado_gerencia',
            name='fecha_aprob',
            field=models.DateTimeField(null=True, verbose_name='Fecha de Aprobación'),
        ),
        migrations.AddField(
            model_name='estado_gerencia',
            name='quien_aprobo',
            field=models.CharField(max_length=60, null=True, verbose_name='Usuario que Aprobó o Denegó'),
        ),
    ]
