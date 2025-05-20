from django.db import models
from django.urls import reverse

class Anio(models.Model):
    anio = models.PositiveIntegerField(unique=True)
    
    class Meta:
        verbose_name = "Año"
        verbose_name_plural = "Años"
        ordering = ['-anio']
    
    def __str__(self):
        return str(self.anio)

class Mes(models.Model):
    MESES = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'),
        (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'),
        (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'),
        (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
    ]
    
    anio = models.ForeignKey(Anio, on_delete=models.CASCADE)
    mes = models.PositiveSmallIntegerField(choices=MESES)
    
    class Meta:
        unique_together = ('anio', 'mes')
        ordering = ['anio', 'mes']
    
    def __str__(self):
        return f"{self.get_mes_display()} {self.anio}"

class Circular(models.Model):
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='circulares/%Y/%m/')
    fecha = models.DateField()
    
    class Meta:
        ordering = ['-fecha', 'numero']
    
    def __str__(self):
        return f"Circular {self.numero} - {self.titulo}"
