from django.db import models

# Create your models here.
class PaginaInicio(models.Model):
    titulo = models.CharField(max_length=200, default='Contraloría UMSNH')
    mision = models.TextField()
    vision = models.TextField()
    quienes_somos = models.TextField()
    organigrama = models.ImageField(upload_to='organigramas/', blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo