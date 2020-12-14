# Generated by Django 3.1 on 2020-10-05 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0004_solicitud_quien_aprobo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='fecha_aprob',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='quien_aprobo',
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.usuario', verbose_name='Cargo Quien Solicita'),
        ),
    ]