# Generated by Django 3.1 on 2020-10-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0003_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='quien_aprobo',
            field=models.CharField(max_length=60, null=True, verbose_name='Usuario que Aprobó'),
        ),
    ]
