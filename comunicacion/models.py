from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#24356B') # Color Insitucional

    def __str__(self):
        return self.nombre
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    destacada = models.BooleanField(default=False)
    enlace_externo = models.URLField(blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.titulo

class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    urgente = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['urgente', '-fecha_inicio']

class RedSocial(models.Model):
    PLATAFORMAS = [
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('IG', 'Instagram')
    ]
    
    plataforma = models.CharField(max_length=2, choices=PLATAFORMAS)
    enlace = models.URLField()
    widget_html = models.TextField(blank=True, help_text="Código embed de Meta Business Suite")

    def __str__(self):
        return self.get_plataforma_display()
