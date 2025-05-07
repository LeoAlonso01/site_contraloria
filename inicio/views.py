from django.shortcuts import render
from .models import PaginaInicio

# Create your views here.
def homne(request):
    pagina = PaginaInicio.objects.first()
    return render(request, 'inicio/home.html', {'pagina': pagina})
