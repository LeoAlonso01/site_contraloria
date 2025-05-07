from django.shortcuts import render
from .models import Jefatura

def directorio_view(request):
    jefaturas = Jefatura.objects.all()
    return render(request, 'directorio/directorio.html', {'jefaturas': jefaturas})
