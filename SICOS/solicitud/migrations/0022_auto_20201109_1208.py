# Generated by Django 3.1 on 2020-11-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0021_auto_20201109_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado_principal',
            name='obs',
            field=models.TextField(default='', verbose_name='Observación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado_secundario',
            name='obs',
            field=models.TextField(default='', verbose_name='Observación'),
            preserve_default=False,
        ),
    ]
