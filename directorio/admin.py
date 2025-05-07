from django.contrib import admin
from .models import Jefatura

@admin.register(Jefatura)
class JefaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'nombramiento', 'telefono')
