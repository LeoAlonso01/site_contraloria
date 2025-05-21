from django.urls import path
from .views import comunicacion, detalle_noticia

urlpatterns = [
    path('comunicacion/', comunicacion, name='comunicacion'),
    path('noticia/<slug:slug>/', detalle_noticia, name='detalle_noticia')
]