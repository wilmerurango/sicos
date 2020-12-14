from django.contrib import admin

from solicitud.models import *

admin.site.register(Usuario)
admin.site.register(Proceso_solicitante)
admin.site.register(UnidadMedida)
admin.site.register(Estado)
admin.site.register(Solicitud)
admin.site.register(Estado_Principal)
admin.site.register(Estado_Secundario)