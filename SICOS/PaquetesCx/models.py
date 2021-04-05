from django.db import models

# Create your models here.
class TipoProcedimiento(models.Model):
    nombre_tipo_proc = models.CharField('Nombre de la Especialidad', null = True, max_length = 80, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_tipo_proc)
    
    class Meta:
        ordering = ['nombre_tipo_proc']


class NombreCanasta(models.Model):
    nombre_canasta = models.CharField('Nombre de la Canasta', null = True, max_length = 85, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_canasta)
    
    class Meta:
        ordering = ['nombre_canasta']


class ConceptoHonorarioSalario(models.Model):
    nombre_concep_hon = models.CharField('Nombre del Concepto', null = True, max_length = 30, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_concep_hon)
    
    class Meta:
        ordering = ['nombre_concep_hon']


class ConceptoCanasta(models.Model):
    nombre_canasta = models.CharField('Concepto de la Canasta', null = True, max_length = 85, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_canasta)
    
    class Meta:
        ordering = ['nombre_canasta']


class Actividad(models.Model):#aqui se escribe a q actividad pertenece el salario (entrada, ciruria, postcirugia, salida , etc)

    nombre_act = models.CharField('Nombre de la Actividad', null = True, max_length = 20, unique=True)
    
    def __str__(self):
        return '%s' % (self.nombre_act)
    
    class Meta:
        ordering = ['nombre_act']


class Constante(models.Model):
    iss_adicional = models.FloatField('Porcentaje Ganancia', null = True)
    valor_uvt = models.FloatField('Valor UVT Especialistas', null = True, default = 0)
    smdlv = models.FloatField('Salaraio Minimo Diario L.V.', null = True, default = 0)
    
    def __str__(self):
        return '%s' % (self.iss_adicional)
    
    class Meta:
        ordering = ['iss_adicional']


class TipoEstancia(models.Model):
    nombre_tipo_est = models.CharField('Tipo de Estancia', null =  True, max_length = 60)
    numero_camas = models.IntegerField('Número de Camas', null =  True, default = 0)

    def __str__(self):
        return '%s' % (self.nombre_tipo_est)


# class ConceptoSalario(models.Model):
#     nombre_concep_sal = models.CharField('Concepto', null = True, max_length = 30, unique=True)
    
#     def __str__(self):
#         return '%s' % (self.nombre_concep_sal)
    
#     class Meta:
#         ordering = ['nombre_concep_sal']


class Cargo(models.Model):
    nombre_cargo = models.CharField('Cargo', null = True, max_length = 30, unique=True)
    descripcion = models.CharField('Descripción de Cargo', null = True, max_length = 30)
    valor = models.FloatField('Valor Costo Salario Mensual')

    def __str__(self):
        return '%s' % (self.nombre_cargo)


class Insumo(models.Model):
    nombre= models.CharField('Nombre del Insumo', null = True, max_length = 30, unique=True)
    codigo = models.CharField('Codigo del Insumo', null = True, max_length = 30)
    presentacion = models.CharField('Presentación', null = True, max_length = 30)
    valor = models.FloatField('Valor Compra')

    def __str__(self):
        return '%s' % (self.nombre_cargo)


class Canasta(models.Model):
    nombreCanasta = models.ForeignKey(NombreCanasta, verbose_name ='Nombre de la Canasta', on_delete=models.PROTECT, null = True, unique=True)
    conceptoCanasta =   models.ForeignKey(ConceptoCanasta,verbose_name = 'Concepto', null = True, on_delete = models.PROTECT)
    actividad =  models.ForeignKey(Actividad, verbose_name ='Ubicación', null = True,blank=True, on_delete = models.PROTECT)
    insumo =  models.ForeignKey(Insumo, verbose_name ='Insumo', null = True,blank=True, on_delete = models.PROTECT)
    cantidad =  models.FloatField('Cantidad', null = True, default = 1)


class Procedimiento(models.Model):
    cod_cup = models.CharField('Código Cups', null = True, max_length = 20, blank = True)
    cod_soat = models.CharField('Código SOAT', null = True, max_length = 20, blank = True)
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Especialidad', null = True, on_delete=models.PROTECT)
    nombre_proc = models.CharField('Nombre del Procedimiento', null = True, max_length = 190, unique=True)
    NombreCanasta = models.ForeignKey(NombreCanasta,verbose_name = 'Canasta', null = True, on_delete=models.PROTECT)
    duracion_proc = models.FloatField('Duración en minutos', null = True)
    uvr =  models.FloatField('UVR', null = True, blank = True, default = 0)
    conts_soat = models.FloatField('Constante SOAT', null = True, blank = True, default = 0)
    dias_estancia = models.IntegerField('Días Estancia', null = True, default = 0)
    
    def __str__(self):
        return '%s' % (self.nombre_proc)


class HonorarioSalario(models.Model):
    salario='SALARIO'
    honorario = 'HONORARIO'
    opcion_choices=[
        (salario,'SALARIO'),
        (honorario,'HONORARIO'),
    ]
    tipo = models.CharField('TIPO DE PAGO',max_length=9,choices=opcion_choices, default=salario)
    conceptoHonorarioSalario = models.ForeignKey(ConceptoHonorarioSalario,verbose_name = 'Concepto', null = True, on_delete=models.PROTECT)
    tipoProcedimiento = models.ForeignKey(TipoProcedimiento,verbose_name = 'Especialidad', null = True, on_delete=models.PROTECT)
    procedimiento = models.ForeignKey(Procedimiento,verbose_name = 'Procedimiento', null = True, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo,verbose_name = 'Cargo', null = True, on_delete=models.PROTECT)
    costo = models.FloatField('Costo no Paramertrizado', null = True, blank = True, default=0)
    actividad =  models.ForeignKey(Actividad, verbose_name ='Ubicación', null = True,blank=True, on_delete = models.PROTECT)


class Estancia(models.Model):
    tipoEstancia = models.ForeignKey(TipoEstancia, null=True, on_delete=models.CASCADE, verbose_name = "Tipo de Estancia")
    concepto_estancia = models.CharField('Concepto Estancia', null = True, max_length = 40)
    valor_concepto = models.FloatField('Valor día',null=True, default = 0)
    dividir_por_cama = models.BooleanField('¿Se divide entre el número de camas ?', default = True)
    
    def __str__(self):
        return '%s' % (self.concepto_estancia)

    