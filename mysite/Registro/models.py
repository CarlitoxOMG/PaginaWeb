from django.db import models

# Create your models here.
class Dueño(models.Model):
    nombre = models.CharField(max_length=20)
    rut = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=50)
    dueño = models.ForeignKey(Dueño, null=True, blank=True, on_delete=models.CASCADE)
    raza = models.CharField(max_length=50)
    domicilio = models.TextField()
    # fecha_registro = models.DateField()

    def __str__(self):
        return self.nombre_mascota