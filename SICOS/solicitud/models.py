from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Proceso_solicitante(models.Model):
    nombre_area = models.CharField('Escriba el nombre del Area Funcional', max_length=60)

    def __str__(self):
        return '%s' % (self.nombre_area)

class Usuario(models.Model):#Este modelo se creo para hcer un CRUD con el modelo User de Django para agregar los campos adicionales requeridos
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True)
    # area = models.CharField('Area o Servicio', max_length=40)
    cargo =  models.CharField('Cargo', max_length= 40)
    proceso_solicitante = models.ForeignKey(Proceso_solicitante, verbose_name='Area Funcional que representa la Necesidad', on_delete=models.CASCADE, null = True)

    # fecha = models.DateField('Fecha de Registro de Usuario')

    def __str__(self):
        return '%s' % (self.user.username)


class UnidadMedida(models.Model):
    nombre_und = models.CharField('Escriba la Unidad de Medida',max_length=20)
    def __str__(self):
        return '%s' % (self.nombre_und)

class Estado(models.Model):
    nombre_estado = models.CharField('Estado',max_length=20)
    def __str__(self):
        return '%s' % (self.nombre_estado)
    

class Solicitud(models.Model):
    unidadMedida = models.ForeignKey(UnidadMedida, verbose_name="Unidad de Medida", on_delete=models.CASCADE)
    cantidad = models.IntegerField('Cantidad', default=1)
    description = models.TextField('Descripción del Articulo o Activo')
    ref = models.CharField('Referencia', max_length=20)
    justificacion = models.TextField('Justificación')
    obs = models.TextField('Observación', blank = True)
    usuario = models.ForeignKey(Usuario, verbose_name='Cargo Quien Solicita', on_delete=models.CASCADE)# Datos de quien realiza la solicitud
    fecha_solici = models.DateTimeField('Fecha de Solicitud')

    def __str__(self):
        return '%s' % (self.ref)

class Estado_Principal(models.Model):#en el caso de clinica dle rio rio es el primer filtro y lo realiza la gerencia
    pendiente = "Pendiente"
    aprobado = "Aprobado"
    denegado = "Denegado"

    opcion_choices=[
        (pendiente,'Pendiente'),
        (aprobado,'Aprobado'),
        (denegado,'Denegado'),
    ]
    
    solicitud = models.OneToOneField(Solicitud, verbose_name="Solicitud", on_delete=models.CASCADE)
    estado = models.CharField("Solicitud",max_length=12,choices=opcion_choices, default=pendiente)
    quien_aprobo = models.CharField('Usuario que Aprobó o Denegó', max_length=60, null=True)
    fecha_aprob = models.DateTimeField('Fecha de Aprobación',  null=True)
    obs = models.TextField('Observación' , blank=True)

class Estado_Secundario(models.Model):
    pendiente = "Pendiente"
    gestionado = "Gestionado"

    opcion_choices=[
        (pendiente,'Pendiente'),
        (gestionado,'Gestionado'),
    ]
    estado_Principal = models.OneToOneField(Estado_Principal, verbose_name="Solicitud", on_delete=models.CASCADE, null=True)
    estado = models.CharField("Solicitud",max_length=12,choices=opcion_choices, default=pendiente)
    quien_aprobo = models.CharField('Usuario que Aprobó o Denegó', max_length=60, null=True)
    fecha_aprob = models.DateTimeField('Fecha de Aprobación',  null=True)
    obs = models.TextField('Observación', blank=True)


