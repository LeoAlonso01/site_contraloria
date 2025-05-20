from django.shortcuts import render
from .models import Anio

def lista_circulares(request):
    años = Anio.objects.prefetch_related('mes_set__circular_set').all()
    return render(request, 'circulares/lista.html', {
        'años': años,
        'seccion_activa': 'circulares'
    })
