FROM python:3.11-slim

# Instala dependencias del sistema
RUN apt-get update 

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY requirements.txt .

# Instala dependencias de Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .
# Expose the port the app runs on
EXPOSE 8000

# Comando por defecto (lo ajustaremos luego)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "contraloria_site.wsgi:application"]