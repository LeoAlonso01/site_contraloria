# enlaces/urls.py
from django.urls import path
from .views import lista_enlaces

urlpatterns = [
    path('', lista_enlaces, name='enlaces'),  # Ruta principal
]