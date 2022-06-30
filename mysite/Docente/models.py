from django.db import models

# Create your models here.
GRADOS_ACADEMICO = (
    ('Tecnico', 'Tecnico'),
    ('Profesional', 'Profesional'),
)

class Docente (models.Model):
    fotografia = models.ImageField(upload_to='docentes')
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    grado_academico = models.CharField(max_length=50, choices=GRADOS_ACADEMICO)

    def __str__(self):
        return str(self.fotografia)

