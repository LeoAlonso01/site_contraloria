from django.shortcuts import render
from .models import Enlace

def lista_enlaces(request):
    enlaces = Enlace.objects.filter(activo=True).order_by('orden')
    return render(request, 'enlaces/lista_enlaces.html', {
        'enlaces': enlaces,
        'seccion_activa': 'enlaces'
    })