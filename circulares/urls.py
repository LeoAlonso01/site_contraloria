from django.urls import path
from .views import lista_circulares

urlpatterns = [
    path('', lista_circulares, name='circulares'),
]