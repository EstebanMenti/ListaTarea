from django import forms
from django.forms import ModelForm

from .models import Tareas


class TareasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for dic in self.fields.keys():
            self.fields[ dic ].widget.attrs.update({'class':'form-control'})

        #self.fields[ 'user_id' ].widget.attrs.update({'class':'form-HiddenInput'})
        #self.fields[ 'status' ].widget.attrs.update({'class':'form-select'})

                
    class Meta:
        model = Tareas
        exclude = ['user_id']
  