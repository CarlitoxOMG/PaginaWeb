from .models import Docente
from django import forms

class DocenteForm(forms.ModelForm):
    

    class Meta:
        model = Docente
        fields = (
            'fotografia',
            'rut',
            'nombre',
            'email',
            'grado_academico'
        )
        labels = {
            'fotografia':'Fotografia',
            'rut':'RUN',
            'nombre':'Nombre',
            'email':'Correo electronico',
            'grado_academico':'Grado Academico'
        }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'grado_academico':forms.Select(choices="GRADOS_ACADEMICO", attrs={'class':'form-control'}),
        }

