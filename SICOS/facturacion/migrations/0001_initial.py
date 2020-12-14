# Generated by Django 3.1 on 2020-08-19 21:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_act', models.CharField(max_length=70, verbose_name='Nombre de la Actividad')),
                ('valor_iss', models.FloatField(default=0, null=True, verbose_name='Valor ISS')),
                ('pct_iss', models.FloatField(default=25, null=True, verbose_name='Porcentaje ISS Adicional (%)')),
            ],
            options={
                'ordering': ['name_act'],
            },
        ),
        migrations.CreateModel(
            name='arriendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_arri', models.CharField(max_length=11, verbose_name='NIT')),
                ('name_arri', models.CharField(max_length=100, verbose_name='Nombre del Tercero')),
                ('tel_arri', models.CharField(max_length=12, verbose_name='Telefono')),
                ('dir_arri', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección')),
                ('mail_arri', models.EmailField(blank=True, max_length=60, null=True, verbose_name='E-mail')),
                ('fechafact_arri', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, null=True, verbose_name='Nombre del Producto')),
                ('descrip', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='centro_actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_centro_act', models.CharField(max_length=70, verbose_name='Nombre Cuenta')),
                ('cuenta', models.BigIntegerField(null=True, verbose_name='N° Cuenta')),
                ('actividad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.actividad', verbose_name='Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='centro_costo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_centro_costo', models.CharField(max_length=20, verbose_name='Número de Cuenta')),
                ('name_ccos', models.CharField(max_length=100, verbose_name='Nombre del Centro de Costo')),
            ],
        ),
        migrations.CreateModel(
            name='contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_esp', models.CharField(blank=True, max_length=70, verbose_name='Especialidad')),
                ('valor', models.FloatField(default=0, verbose_name='Monto Devengado al mes')),
                ('info_contrato', models.TextField(blank=True, null=True, verbose_name='Información sobre el contrato')),
                ('razon_social_reglament', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Razon Social Reglamentaria')),
                ('reten_11', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Retención 11%')),
                ('reten_art_383', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Aplica Retención Art. 383')),
                ('aporte_arl', models.FloatField(default=0, verbose_name='Porcentaje Aportes de Pension')),
                ('dependiente_cargo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Dependiente a Cargo')),
                ('reten_10', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Retención del 10%')),
                ('pension_obligado', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Obligado a Cotizar Pension ')),
                ('reten_arrindo', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Retención por Arriendo')),
                ('fecha', models.DateField(default=datetime.datetime(2020, 8, 19, 21, 22, 4, 726506, tzinfo=utc), verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_arriendo_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpp_arriendo', models.IntegerField(null=True, verbose_name='N° Factura')),
                ('name_arri', models.CharField(max_length=150, null=True, verbose_name='Nombre Empresa')),
                ('centro_costo', models.CharField(max_length=100, null=True, verbose_name='Centro de Costo')),
                ('inductor_arri', models.FloatField(default=0, verbose_name='Inductor')),
                ('num_cuenta', models.CharField(max_length=100, null=True, verbose_name='Cuenta C. Costo')),
                ('cuenta_especific', models.CharField(max_length=100, null=True, verbose_name='Cuenta Especifica')),
                ('valor_cpp_arri_detal', models.FloatField(default=0, verbose_name='Valor')),
                ('fecha_cpp_arri_detal', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_factura', models.FloatField(default=0, verbose_name='Valor Factura')),
                ('aire_medicinal', models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿corresponde a arriendo de aire medicinal?')),
                ('reten', models.FloatField(default=0, null=True, verbose_name='Retención')),
                ('valor_cpp_prov', models.FloatField(default=0, null=True, verbose_name='Valor')),
                ('fecha_cpp_prov', models.DateField(null=True, verbose_name='Fecha')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='cpp_proveedor_subdetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpp_proveedor', models.IntegerField(default=0, null=True, verbose_name='N° de CPP')),
                ('centro_costo', models.IntegerField(blank=True, default=0, null=True, verbose_name='Centro de Costo')),
                ('proveedor', models.IntegerField(null=True, verbose_name='Nit del Proveedor')),
                ('cant_produc', models.FloatField(default=0, null=True, verbose_name='Cantidad Productos')),
                ('cant_flete', models.FloatField(default=0, null=True, verbose_name='Cantidad Flete')),
                ('valor_flete', models.FloatField(default=0, null=True, verbose_name='Valor Flete')),
                ('nombre_cuenta', models.CharField(max_length=70, null=True, verbose_name='Nombre de la Cuenta')),
                ('cuenta', models.CharField(max_length=20, null=True, verbose_name='Número de Cuenta')),
                ('naturaleza_cuenta', models.CharField(max_length=8, null=True, verbose_name='Naturaleza de la Cuenta')),
                ('distrib', models.FloatField(default=0, null=True, verbose_name='% Distribución')),
                ('name_centro_costo', models.CharField(max_length=70, null=True, verbose_name='Nombre Centro Costo')),
                ('costo', models.FloatField(default=0, null=True, verbose_name='Costo')),
                ('cuenta_iva', models.CharField(max_length=20, null=True, verbose_name='Cuenta Iva')),
                ('valor_iva', models.FloatField(default=0, null=True, verbose_name='Valor Iva')),
                ('valor_cuenta_contra', models.FloatField(default=0, null=True, verbose_name='valor Cuenta Contra')),
                ('fecha_cpp_prov_detal', models.DateField(null=True, verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_servi_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpp_serv_public', models.IntegerField(null=True, verbose_name='ID CPP')),
                ('id_serv_public', models.IntegerField(null=True, verbose_name='ID Servicio Público')),
                ('name_serv_public', models.CharField(max_length=50, null=True, verbose_name='Nombre del Tercero')),
                ('id_centro_costo', models.IntegerField(null=True, verbose_name='ID Centro Costo')),
                ('name_ccos', models.CharField(max_length=50, null=True, verbose_name='Nombre Centro de Costo')),
                ('distri', models.FloatField(default=0, null=True, verbose_name='Disctribución (%)')),
                ('name_cuenta_aux', models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta')),
                ('num_cuenta_aux', models.CharField(max_length=20, null=True, verbose_name='Número Cuenta')),
                ('costo', models.FloatField(default=0, null=True, verbose_name='Costo Asignado')),
                ('num_cuenta_iva', models.CharField(blank=True, max_length=20, null=True, verbose_name='Num. Cuenta de Iva')),
                ('valor_iva', models.FloatField(default=0, null=True, verbose_name='Valor del Iva')),
                ('valor_contra', models.FloatField(default=0, null=True, verbose_name='Valor Contra')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_servicio_medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_sm', models.FloatField(default=0, verbose_name='Valor')),
                ('fecha_cpp_sm', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='especialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_esp', models.CharField(max_length=11, verbose_name='Identificación')),
                ('name_esp', models.CharField(max_length=50, verbose_name='Nombre del Especialista')),
                ('apellidos_esp', models.CharField(blank=True, max_length=70, verbose_name='Apellidos del Especialista')),
                ('especialidad', models.CharField(default='No se Registro', max_length=50, verbose_name='Especialidad')),
                ('tel_esp', models.CharField(blank=True, max_length=12, verbose_name='Telefono')),
                ('dir_esp', models.CharField(blank=True, max_length=100, verbose_name='Dirección')),
                ('mail_esp', models.EmailField(blank=True, max_length=60, verbose_name='E-mail')),
                ('fechafact_esp', models.DateField(default=datetime.datetime(2020, 8, 19, 21, 22, 4, 726506, tzinfo=utc), verbose_name='Fecha de Registro')),
            ],
        ),
        migrations.CreateModel(
            name='fac_especialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glosa', models.FloatField(default=0, null=True, verbose_name='Glosa del mes')),
                ('valor', models.FloatField(default=0, null=True)),
                ('acum', models.FloatField(default=0, null=True)),
                ('aport_volun_pension', models.FloatField(default=0, null=True, verbose_name='Aportes Voluntarios a Pension Max 25% S.')),
                ('int_pre_vivi', models.FloatField(default=0, null=True, verbose_name='Intereses Prestamo de Vivienda Max 100 UVT ')),
                ('plan_comp_salud', models.FloatField(default=0, null=True, verbose_name='Plan Complementrio de Salud ')),
                ('aport_afc', models.FloatField(default=0, null=True, verbose_name='Aportes a Cuentas AFC')),
                ('aport_volun_emple', models.FloatField(default=0, null=True, verbose_name='Aportes Voluntarios del Empleador')),
                ('indem_lab', models.FloatField(default=0, null=True, verbose_name='Indemnizaciones Laborales')),
                ('rent_exten_lab', models.FloatField(default=25, null=True, verbose_name='Renta Extensa Laboral')),
                ('top_deduc_rent_exte', models.FloatField(default=40, null=True, verbose_name='Tope Deducciones + Renta Extensa ')),
                ('fecha_pagada', models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], default='Enero', max_length=15, verbose_name='Mes Pagado')),
                ('fechafac_esp', models.DateField(default=datetime.datetime(2020, 8, 19, 21, 22, 4, 726506, tzinfo=utc), verbose_name='Fecha de Registro')),
                ('especialista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.especialista', verbose_name='Identificación')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit_prov', models.CharField(max_length=11, null=True, verbose_name='NIT')),
                ('name_prov', models.CharField(max_length=100, verbose_name='Nombre del Proveedor')),
                ('distri_fija', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='¿Distribución Porcentual?')),
                ('dir_prov', models.CharField(blank=True, max_length=100, verbose_name='Dirección')),
                ('tel_prov', models.CharField(blank=True, max_length=12, verbose_name='Telefono')),
                ('mail_prov', models.EmailField(blank=True, max_length=60, verbose_name='E-mail')),
                ('fecharegistro_prov', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='retencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_especialista', models.IntegerField(default=0, null=True, verbose_name='Códido Especialista')),
                ('name_especialista', models.CharField(max_length=30, null=True, verbose_name='Nombre Especialista')),
                ('honorario', models.FloatField(default=0, null=True, verbose_name='Honorario')),
                ('incr_aport_pension', models.FloatField(default=0, null=True, verbose_name='Aportes a Pension')),
                ('incr_solida_pensional', models.FloatField(default=0, null=True, verbose_name='Solidaridad Pensional')),
                ('incr_aport_salud', models.FloatField(default=0, null=True, verbose_name='Aportes a Salud')),
                ('incr_aport_arl', models.FloatField(default=0, null=True, verbose_name='Aportes a ARL')),
                ('incr_aport_vol_pension', models.FloatField(default=0, null=True, verbose_name='Aportes Voluntarios a Pension')),
                ('deduc_int_prest_vivienda', models.FloatField(default=0, null=True, verbose_name='Intereses Prestamo Viviendas')),
                ('deduc_plan_comp_salud', models.FloatField(default=0, null=True, verbose_name='Plan Complementario Salud')),
                ('deduc_depen_cargo', models.FloatField(default=0, null=True, verbose_name='Dependinte de Cargo')),
                ('aport_cuenta_afc', models.FloatField(default=0, null=True, verbose_name='Aporte Renta Exenta')),
                ('aport_volun_empleador', models.FloatField(default=0, null=True, verbose_name='Aporte Voluntario Empleador')),
                ('indemni_lab', models.FloatField(default=0, null=True, verbose_name='Indemnizaciones Laborales')),
                ('re_rent_exent_lab', models.FloatField(default=0, null=True, verbose_name='Renta Exenta Laboral')),
                ('re_deduc_rent_exent', models.FloatField(default=0, null=True, verbose_name='Total Deducciones + Renta Exenta')),
                ('re_tope_rent_exent_lab', models.FloatField(default=0, null=True, verbose_name='Tope Deducciones + Renta Exenta')),
                ('re_total_base_grav_reten', models.FloatField(default=0, null=True, verbose_name='Total Base Gravable para Retención')),
                ('re_base_grav_reten_uvt', models.FloatField(default=0, null=True, verbose_name='Base Gravable en UVT')),
                ('re_fuente_uvt', models.FloatField(default=0, null=True, verbose_name='Retenccion en la Fuente Expresada en UVT')),
                ('re_valor_reten', models.FloatField(default=0, null=True, verbose_name='Valor Retención')),
            ],
        ),
        migrations.CreateModel(
            name='servicio_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit_sgen', models.CharField(max_length=11, verbose_name='NIT')),
                ('name_sgen', models.CharField(max_length=100, verbose_name='Nombre el la Empresa')),
                ('tel_sgen', models.CharField(max_length=12, verbose_name='Telefono')),
                ('dir_sgen', models.CharField(max_length=100, verbose_name='Dirección')),
                ('mail_sgen', models.EmailField(max_length=60, verbose_name='E-mail')),
                ('fechafact_sgen', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='servicio_medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit_servm', models.CharField(max_length=11, verbose_name='NIT')),
                ('name_servm', models.CharField(max_length=100, verbose_name='Nombre del Servicio')),
                ('tel_servm', models.CharField(max_length=12, verbose_name='Telefono')),
                ('dir_servm', models.CharField(max_length=100, verbose_name='Dirección')),
                ('mail_servm', models.EmailField(max_length=60, verbose_name='E-mail')),
                ('fechafact_servm', models.DateField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='sub_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subactivity', models.CharField(max_length=70, verbose_name='Nombre de la Categoria')),
            ],
            options={
                'ordering': ['name_subactivity'],
            },
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True, verbose_name='Tarifa')),
                ('fecha_inicio', models.DateField(null=True, verbose_name='Fecha Inicio')),
                ('fecha_final', models.DateField(blank=True, null=True, verbose_name='Fecha Final')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fact', models.CharField(max_length=20, verbose_name='Nombre del Tipo de Facturación')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_serv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo', models.CharField(max_length=70, null=True, verbose_name='Tipo de Servicio')),
                ('descrip', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='uvt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_uvt', models.FloatField(default=34270, null=True, verbose_name='Valor del UVT')),
                ('smlv', models.FloatField(default=828116, null=True, verbose_name='Valor Salario Minimo')),
                ('restric_smlv', models.FloatField(default=0, null=True, verbose_name='Restricción SMLV')),
                ('rent_ext_lab', models.FloatField(default=0, null=True, verbose_name='Renta Extensa Laboral en %')),
                ('tope_deduc_re', models.FloatField(default=0, null=True, verbose_name='Tope Renta Extensa en %')),
                ('tarifa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tarifa', verbose_name='Nombre Tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=15, null=True, verbose_name='NIT')),
                ('nombre_tercero', models.CharField(max_length=50, null=True, verbose_name='Nombre Tercero')),
                ('nombre_serv', models.CharField(max_length=50, null=True, verbose_name='Nombre Servicio')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Dirección')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('tipo_serv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tipo_serv', verbose_name='Tipo de Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='reten_383',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimo', models.FloatField(default=0, null=True, verbose_name='Minimo')),
                ('maximo', models.FloatField(default=0, null=True, verbose_name='Máximo')),
                ('resta', models.FloatField(default=0, null=True, verbose_name='Resta')),
                ('porcent', models.FloatField(default=0, null=True, verbose_name='Porcentaje')),
                ('adicion', models.FloatField(default=0, null=True, verbose_name='Adicion Puntos')),
                ('tarifa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tarifa', verbose_name='Nombre Tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, null=True, verbose_name='Nombre del Producto')),
                ('precio', models.FloatField(default=0, null=True, verbose_name='Precio del Producto')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.categoria', verbose_name='Categoria')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='inductor_arri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta_especific', models.CharField(max_length=20, null=True, verbose_name='Cuenta Específica')),
                ('induc', models.FloatField(verbose_name='Inductor en %')),
                ('fecha_induc', models.DateField(null=True, verbose_name='Fecha de Actualizacion')),
                ('arriendo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.arriendo', verbose_name='Nombre del Tercero')),
                ('centro_costo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro Costo')),
            ],
        ),
        migrations.CreateModel(
            name='fac_especialista_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0, null=True)),
                ('fechafac_detalle', models.DateField(null=True, verbose_name='Fecha')),
                ('parametrizado', models.BooleanField(default=True, verbose_name='¿Pamametrizado?')),
                ('centro_actividad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_actividad', verbose_name='Actividad')),
                ('centro_costo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo')),
                ('fac_especialista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.fac_especialista', verbose_name='Codigo de la Factura')),
                ('tipo_fact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tipo_fact', verbose_name='Tipo de Factura o CPP')),
            ],
        ),
        migrations.AddField(
            model_name='fac_especialista',
            name='tarifa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tarifa', verbose_name='Nombre Tarifa'),
        ),
        migrations.CreateModel(
            name='especialista_cpp_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.contrato', verbose_name='Identificación Especialista')),
                ('tipo_fact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.tipo_fact', verbose_name='Tipo Facturacion')),
            ],
        ),
        migrations.CreateModel(
            name='distribucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cuenta', models.CharField(max_length=70, null=True, verbose_name='Nombre de la Cuenta')),
                ('naturaleza_cuenta', models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], default='Credito', max_length=8, verbose_name='Naturaleza de la Cuenta')),
                ('cuenta', models.CharField(max_length=20, null=True, verbose_name='Número de Cuenta')),
                ('distrib', models.FloatField(default=0, null=True, verbose_name='% Distribución')),
                ('meneja_iva', models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, null=True, verbose_name='¿Maneja Iva?')),
                ('cuenta_iva', models.CharField(blank=True, max_length=20, null=True, verbose_name='Numero Cuenta de Iva')),
                ('valor_iva', models.FloatField(blank=True, default=0, null=True, verbose_name='Porcentaje Iva')),
                ('centro_costo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.producto', verbose_name='Producto')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.proveedor', verbose_name='Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='distri_serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta_especific', models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta Especifica')),
                ('num_cuenta_especific', models.CharField(max_length=50, null=True, verbose_name='Número Cuenta Especifica')),
                ('distri', models.FloatField(default=0, null=True, verbose_name='Disctribución (%)')),
                ('cuenta_iva', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cuenta de Iva')),
                ('num_cuenta_iva', models.CharField(blank=True, max_length=20, null=True, verbose_name='Num. Cuenta de Iva')),
                ('fecha_distri', models.DateField(null=True, verbose_name='Fecha')),
                ('centro_costo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='cuenta_reten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta', models.CharField(max_length=50, verbose_name='Nombre de Cuenta')),
                ('num_cuenta', models.BigIntegerField(null=True, verbose_name='Número de Cuenta')),
                ('porc_retencion', models.FloatField(default=4, null=True, verbose_name='Retención en %')),
                ('contrato', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.contrato', verbose_name='Base Retención-Especialista')),
            ],
        ),
        migrations.CreateModel(
            name='cuenta_aux_serv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta', models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta')),
                ('num_cuenta', models.CharField(max_length=20, null=True, verbose_name='Número Cuenta')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del servicio')),
            ],
        ),
        migrations.CreateModel(
            name='cuenta_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta', models.CharField(max_length=50, null=True, verbose_name='Nombre de la Cuenta')),
                ('cuenta', models.CharField(max_length=50, null=True, verbose_name='Número de la Cuenta')),
                ('naturaleza_cuenta', models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], default='Credito', max_length=8, verbose_name='Naturaleza de la Cuenta')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.proveedor', verbose_name='Seleccionar Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='cuenta_arriendo_aux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta', models.CharField(max_length=50, null=True, verbose_name='Nombre de la Cuenta')),
                ('cuenta', models.CharField(max_length=50, null=True, verbose_name='Número de la Cuenta')),
                ('naturaleza_cuenta', models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], default='Credito', max_length=8, verbose_name='Naturaleza de la Cuenta')),
                ('arriendo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.arriendo', verbose_name='Seleccionar Arriendo')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_servicio_medico_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_sm_detalle', models.FloatField(null=True)),
                ('fecha_sm_detalle', models.DateField(null=True, verbose_name='Fecha')),
                ('actividad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.actividad', verbose_name='Actividad')),
                ('centro_costo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Cuenta Centro de Costo')),
                ('cpp_servicio_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.cpp_servicio_medico', verbose_name='Codigo Servicio Medico')),
                ('sub_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.sub_activity', verbose_name='Subactividad')),
            ],
        ),
        migrations.AddField(
            model_name='cpp_servicio_medico',
            name='servicio_medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturacion.servicio_medico', verbose_name='Nit Servicio Medico'),
        ),
        migrations.CreateModel(
            name='cpp_serv_public',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField(default=0, null=True, verbose_name='Valor Factura')),
                ('iva', models.FloatField(default=0, null=True, verbose_name='% Iva')),
                ('reten', models.FloatField(default=0, null=True, verbose_name='Retención')),
                ('total', models.FloatField(default=0, null=True, verbose_name='Costo Total')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='cpp_proveedor_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_produc', models.FloatField(default=0, null=True, verbose_name='Cantidad Productos')),
                ('valor_produc', models.FloatField(blank=True, default=0, null=True, verbose_name='Valor del Producto')),
                ('cant_flete', models.FloatField(default=0, null=True, verbose_name='Cantidad Flete')),
                ('valor_flete', models.FloatField(default=0, null=True, verbose_name='Valor Flete')),
                ('fecha_cpp_prov_detal', models.DateField(null=True, verbose_name='Fecha')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.categoria', verbose_name='Categoria')),
                ('centro_costo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo')),
                ('cpp_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.cpp_proveedor', verbose_name='N° de Factura')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.producto', verbose_name='Producto')),
            ],
        ),
        migrations.AddField(
            model_name='cpp_proveedor',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.producto', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='cpp_proveedor',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.proveedor', verbose_name='Nit del Proveedor'),
        ),
        migrations.CreateModel(
            name='cpp_arriendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_cpp_arri', models.FloatField(default=0, null=True, verbose_name='Valor de la Factura')),
                ('reten', models.FloatField(default=0, null=True, verbose_name='Retencion en %')),
                ('valor_cont', models.FloatField(default=0, null=True, verbose_name='Valor Contabilizado')),
                ('fecha_cpp_arri', models.DateField(null=True, verbose_name='Fecha')),
                ('arriendo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.arriendo', verbose_name='Nombre del Tercero')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='especialista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.especialista', verbose_name='Nombre del Especialista'),
        ),
        migrations.AddField(
            model_name='centro_actividad',
            name='centro_costo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.centro_costo', verbose_name='Centro de Costo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='sub_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.sub_activity', verbose_name='Grupo de la Actividad'),
        ),
    ]
