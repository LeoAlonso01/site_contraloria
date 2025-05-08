from django.db import models

class Enlace(models.Model):
    TIPO_CHOICES = [
        ('DOC', 'Documento'),
        ('EXT', 'Aplicación Externa'),
        ('PAG', 'Página Web'),
    ]
    
    nombre = models.CharField(max_length=100)
    url = models.URLField()
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, default='DOC')
    imagen = models.ImageField(
        upload_to='enlaces/',
        blank=True,
        null=True,
        help_text="Logo o imagen representativa (recomendado 300x300px)"
    )
    icono = models.CharField(
        max_length=50, 
        default='bi bi-link-45deg',
        help_text="Clase de Bootstrap Icons (opcional si no hay imagen)"
    )
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Enlaces"
        ordering = ['orden']

    def __str__(self):
        return self.nombre

    def tipo_icono(self):
        icons = {
            'DOC': 'bi-file-earmark-text',
            'EXT': 'bi-box-arrow-up-right',
            'PAG': 'bi-globe'
        }
        return icons.get(self.tipo, 'bi-link-45deg')
