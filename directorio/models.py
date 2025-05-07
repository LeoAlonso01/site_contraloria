from django.db import models

# Create your models here.
class Jefatura(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    nombramiento = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)

    def __str__(self):
        return self.nombre
