from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.shortcuts import render , redirect
from solicitud.forms import *
from django.http import JsonResponse
from django.core import serializers
import json
import datetime 

class Crear_User(CreateView): #crear usuario
    model = Usuario
    template_name = 'usuario/usuario.html'
    form_class = UsuarioForm
    second_form_class = UserForm
    success_url = reverse_lazy('home')

    def get_context_data(self,**kwargs):
        context = super(Crear_User, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            usuario = form.save(commit =False)
            usuario.user = form2.save()
            usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
          return render(request,'usuario/usuario_error.html')
            # return self.render_to_response(self.get_context_data(form = form, form2 = form2))



def SolicitudCrear(request):
    _user = User.objects.get(id = request.user.id)
    usuari = Usuario.objects.get(user = _user)
    solici = Solicitud.objects.filter(usuario = usuari )

    if request.method == 'POST' :
        form = SolicitudForm(request.POST)
        if form.is_valid(): 
            form.save()

            ultima_solicitud = Solicitud.objects.last() # llamar la ultima solicitud, la cual es la que acaba de guardarse

            copia_gerencia = Estado_Principal()  #apenas se guarda la solicitud se crea una copia a gerencia para aprobarla o denegarla
            copia_gerencia.solicitud = ultima_solicitud 
            copia_gerencia.save()

            copia_compras = Estado_Secundario()  #apenas se guarda la solicitud se crea una copia a compras para gestionarla, eso solo sucede si la gerencia aprueba dicha solicitud
            copia_compras.estado_Principal = copia_gerencia 
            copia_compras.save()

        return redirect('crear_solicitud')
    else:
        instancia = Solicitud()
        instancia.usuario = Usuario.objects.get(user = _user)
        form = SolicitudForm(instance = instancia)

    return render(request, 'solicitud/Solicitud_form.html', {'form':form, 'solicituds':solici} )



def Estado_PrincipalList(request):
    Estado_Principal_pendiente = Estado_Principal.objects.filter(estado="pendiente")
    Estado_Principal_aprobado = Estado_Principal.objects.filter(estado="aprobado")
    Estado_Principal_denegado = Estado_Principal.objects.filter(estado="denegado")

    contexto = {'Estado_Principals':Estado_Principal_pendiente, 'Estado_Principals_apro':Estado_Principal_aprobado, 'Estado_Principals_dene':Estado_Principal_denegado }
    return render(request, 'solicitud/Estado_Principal_list.html',contexto)

def Estado_PrincipalElim(request, _id):
    Estado_Principal_tem = Estado_Principal.objects.get(id = _id)
    Estado_Principal_tem.delete()
    return redirect('Estado_Principal_list')

def Estado_PrincipalEdit(request,id_):
    _user = User.objects.get(id = request.user.id)
    Estado_Principal1 = Estado_Principal.objects.get(id = id_)
    Estado_Principal1.quien_aprobo = _user
    # Estado_Principal1.fecha_aprob = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if request.method == 'GET':
        form = Estado_PrincipalForm(instance = Estado_Principal1)
    else:
        form = Estado_PrincipalForm(request.POST, instance = Estado_Principal1)
        if form.is_valid():
            form.save()
        return redirect('Filtro_Gerencia_list')

    soli =  Solicitud.objects.get(id = Estado_Principal1.solicitud.id)

    contexto = {'form':form,'solicitud':soli }
    return render(request, 'solicitud/Estado_Principal_form.html',contexto) 


def Estado_SecundarioList(request):
    Estado_Secundario_pendiente = Estado_Secundario.objects.filter(estado="pendiente").filter(estado_Principal__estado="aprobado")
    Estado_Secundario_gestionado = Estado_Secundario.objects.filter(estado="gestionado").filter(estado_Principal__estado="aprobado")
    Estado_Secundario_dene = Estado_Secundario.objects.filter(estado="pendiente").filter(estado_Principal__estado="denegado")

    contexto = {'Estado_Secundarios':Estado_Secundario_pendiente, 'Estado_Secundarios_gest':Estado_Secundario_gestionado, 'Estado_Secundario_dene':Estado_Secundario_dene}
    return render(request, 'solicitud/Estado_Secundario_list.html',contexto)

def Estado_SecundarioElim(request, _id):
    Estado_Secundario_tem = Estado_Secundario.objects.get(id = _id)
    Estado_Secundario_tem.delete()
    return redirect('Estado_Secundario_list')

def Estado_SecundarioEdit(request,id_):
    _user = User.objects.get(id = request.user.id)
    Estado_Secundario1 = Estado_Secundario.objects.get(id = id_)
    Estado_Secundario1.quien_aprobo = _user
    # Estado_Principal1.fecha_aprob = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if request.method == 'GET':
        form = Estado_SecundarioForm(instance = Estado_Secundario1)
    else:
        form = Estado_SecundarioForm(request.POST, instance = Estado_Secundario1)
        if form.is_valid():
            form.save()
        return redirect('Estado_Secundario_list')

    soli =  Solicitud.objects.get(id = Estado_Secundario1.estado_Principal.solicitud.id)
    
    contexto = {'form':form,'solicitud':soli, 'estado_prin':Estado_Secundario1 }
    return render(request, 'solicitud/Estado_Secundario_form.html',contexto) 