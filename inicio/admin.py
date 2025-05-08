from django.contrib import admin
from .models import PaginaInicio

# Register your models here.
class PaginaInicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_actualizacion') # Cambia 'fecha_actualizacion' por el campo que quieras mostrar
    fieldsets = (
        ('Contenido Principal', {
            'fields': ('titulo', 'mision', 'vision', 'quienes_somos') # Cambia 'quienes_somos' por el campo que quieras mostrar
        }),
        ('Imágenes', {
            'fields': ('organigrama', 'banner', 'texto_banner') # Cambia 'texto_banner' por el campo que quieras mostrar
        }),
    )

admin.site.register(PaginaInicio, PaginaInicioAdmin) # Cambia 'PaginaInicio' por el nombre de tu modelo
