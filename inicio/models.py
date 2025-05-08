from django.db import models

# Create your models here.
class PaginaInicio(models.Model):
    titulo = models.CharField(max_length=200, default='Contraloría UMSNH')
    mision = models.TextField()
    vision = models.TextField()
    quienes_somos = models.TextField()
    organigrama = models.ImageField(upload_to='organigramas/', blank=True, null=True)

     # Nuevo campo para el banner
    banner = models.ImageField(
        upload_to='banners/',
        blank=True,
        null=True,
        help_text="Banner principal (recomendado 1920x600 px)"
    )
    texto_banner = models.CharField(
        max_length=200,
        blank=True,
        help_text="Texto descriptivo para el banner"
    )
    
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.titulo