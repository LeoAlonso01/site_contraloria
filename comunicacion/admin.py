from django.contrib import admin
from .models import *

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'destacada')
    list_filter = ('categoria', 'destacada')
    search_fields = ('titulo', 'contenido')
    # prepopulated_fields = {'slug': ('titulo',)}
    

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_inicio', 'fecha_fin', 'urgente')
    list_editable = ('urgente',)

@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display = ('plataforma', 'enlace')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')