from django.contrib import admin
from .models import Enlace
from django.utils.html import format_html

@admin.register(Enlace)
class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'mostrar_imagen', 'orden', 'activo')  # Añadí 'orden' aquí
    list_editable = ('orden', 'activo')  # Ahora 'orden' está en list_display
    list_filter = ('tipo', 'activo')
    search_fields = ('nombre', 'url')
    
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.imagen.url)
        return "Sin imagen"
    mostrar_imagen.short_description = 'Vista previa'