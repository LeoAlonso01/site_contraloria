"""
URL configuration for contraloria_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('directorio/', include('directorio.urls')),
    path('enlaces/', include('enlaces.urls')),  # Nueva línea para los enlaces
    path('circulares/', include('circulares.urls')),  # Nueva línea para las circulares
    path('comunicacion/', include('comunicacion.urls')), # Nueva línea para la app de comunicación
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para las imágenes

