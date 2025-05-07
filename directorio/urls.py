from django.urls import path
from . import views

urlpatterns = [
    path('', views.directorio_view, name='directorio'),
]
