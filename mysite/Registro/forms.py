from django import forms
from .models import Mascota, Dueño

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre_mascota', 'raza', 'domicilio']

        labels = {
            'nombre_mascota': 'Nombre',
            'raza': 'Raza',
            'domicilio': 'Domicilio',
            # 'fecha_registro': 'Fecha_registro',

        }
        widgets = {
            'nombre-mascota': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'fecha_registro': forms.TextInput(attrs={'class': 'form-control'}),
        }
