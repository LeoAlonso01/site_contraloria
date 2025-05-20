from django.contrib import admin
from .models import Anio, Mes, Circular

class MesInline(admin.TabularInline):
    model = Mes
    extra = 0

class CircularInline(admin.TabularInline):
    model = Circular
    extra = 1
    fields = ('numero', 'titulo', 'archivo', 'fecha')

@admin.register(Anio)
class AnioAdmin(admin.ModelAdmin):
    inlines = [MesInline]
    list_display = ('anio',)

@admin.register(Mes)
class MesAdmin(admin.ModelAdmin):
    inlines = [CircularInline]
    list_display = ('anio', 'mes')
    list_filter = ('anio',)

@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'mes', 'fecha')
    search_fields = ('numero', 'titulo')
    list_filter = ('mes__anio', 'mes__mes')
