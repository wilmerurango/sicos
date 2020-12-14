from django.urls import path
from django.contrib.auth.decorators import login_required

from solicitud.api import UserAPI# apis
from solicitud.views import *

urlpatterns = [
    
    path('Crear_Usuario/', UserAPI.as_view(), name='crear_usuario'),#crear usuario con una api

    path('Crear_User/', Crear_User.as_view(), name='Crear_User'),#crear usuario normalmnete

    path('crear_solicitud/', login_required(SolicitudCrear), name ='crear_solicitud'),


    path('Filtro_Gerencia_list/', login_required(Estado_PrincipalList), name ='Filtro_Gerencia_list'),
    path('Filtro_Gerencia_elim/', login_required(Estado_PrincipalElim), name ='Filtro_Gerencia_elim'),
    path('Filtro_Gerencia_edit/<int:id_>/', login_required(Estado_PrincipalEdit), name ='Filtro_Gerencia_edit'),

    path('Estado_Secundario_list/', login_required(Estado_SecundarioList), name ='Estado_Secundario_list'),
    path('Estado_Secundario_elim/', login_required(Estado_SecundarioElim), name ='Estado_Secundario_elim'),
    path('Estado_Secundario_edit/<int:id_>/', login_required(Estado_SecundarioEdit), name ='Estado_Secundario_edit'),
]