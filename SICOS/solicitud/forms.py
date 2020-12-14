from django import forms
from solicitud.models import *
from django.contrib.auth.models import User
import datetime 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        
        fields=(
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        
        fields=(
            '__all__' 
        )

    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            }) 
        self.fields['description'].widget.attrs.update({  
                'style': 'margin-top: 0px; margin-bottom: 0px; height: 94px;'  
            })  
        self.fields['justificacion'].widget.attrs.update({  
                'style': 'margin-top: 0px; margin-bottom: 0px; height: 94px;'  
            })  

        self.fields['obs'].widget.attrs.update({  
                'style': 'margin-top: 0px; margin-bottom: 0px; height: 94px;'  
            })  
            
        self.fields['fecha_solici'].widget.attrs.update({
            'readonly' : True,
            'value':datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Estado_PrincipalForm(forms.ModelForm):
    class Meta:
        model = Estado_Principal
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })  

        self.fields['quien_aprobo'].widget.attrs.update({ 
                'readonly' : True,
            })
        
        self.fields['solicitud'].widget.attrs.update({ 
                'style' : "display:none",
            }) 

        self.fields['obs'].widget.attrs.update({ 
                'style' : "margin-top: 0px; margin-bottom: 0px; height: 97px;",
            }) 
            

        self.fields['fecha_aprob'].widget.attrs.update({
            'readonly' : True,
            'value':datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Estado_SecundarioForm(forms.ModelForm):
    class Meta:
        model = Estado_Secundario
        
        fields=(
            '__all__'
        )
        
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in iter(self.fields):  
            self.fields[field].widget.attrs.update({  
                'class': 'form-control'  
            })     
        self.fields['estado_Principal'].widget.attrs.update({ 
                'style' : "display:none",
            })

        self.fields['quien_aprobo'].widget.attrs.update({ 
                'readonly' : True,
            })

        self.fields['fecha_aprob'].widget.attrs.update({
            'readonly' : True,
            'value':datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

        self.fields['obs'].widget.attrs.update({ 
                'style' : "margin-top: 0px; margin-bottom: 0px; height: 97px;",
            }) 