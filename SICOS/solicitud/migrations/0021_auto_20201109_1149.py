# Generated by Django 3.1 on 2020-11-09 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0020_auto_20201030_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado_secundario',
            name='solicitud',
        ),
        migrations.AddField(
            model_name='estado_secundario',
            name='estado_Principal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.estado_principal', verbose_name='Solicitud'),
        ),
    ]
