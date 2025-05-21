from django.shortcuts import render, get_object_or_404
from .models import Noticia, Aviso, RedSocial
from django.utils import timezone

def comunicacion(request):
    noticias = Noticia.objects.filter(destacada=True)[:5]
    avisos = Aviso.objects.filter(fecha_fin__gte=timezone.now())
    facebook = RedSocial.objects.filter(plataforma='FB').first()
    
    return render(request, 'comunicacion/news.html', {  # Cambiado a news.html
        'noticias': noticias,
        'avisos': avisos,
        'facebook_widget': facebook.widget_html if facebook else None
    })

def detalle_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    noticias_relacionadas = Noticia.objects.filter(
        categoria=noticia.categoria
    ).exclude(id=noticia.id)[:3]
    avisos_urgentes = Aviso.objects.filter(
        urgente=True,
        fecha_fin__gte=timezone.now()
    )[:2]
    
    return render(request, 'comunicacion/detalle.html', {
        'noticia': noticia,
        'noticias_relacionadas': noticias_relacionadas,
        'avisos_urgentes': avisos_urgentes
    })