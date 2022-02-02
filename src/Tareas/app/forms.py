from django import forms
from django.forms import ModelForm

from .models import Usuarios, Tareas

class TareasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for dic in self.fields.keys():
            self.fields[ dic ].widget.attrs.update({'class':'form-control'})

        #self.fields[ 'curso' ].widget.attrs.update({'class':'form-select'})
        #self.fields[ 'status' ].widget.attrs.update({'class':'form-select'})

                
    class Meta:
        model = Tareas
        fields = ['name', 'status', 'comentarios','date_expiration']