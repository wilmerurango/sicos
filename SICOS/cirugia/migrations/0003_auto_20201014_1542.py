# Generated by Django 3.1 on 2020-10-14 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0002_procedimiento_canasta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='procedimiento',
            old_name='canasta',
            new_name='nombre_canasta',
        ),
    ]
