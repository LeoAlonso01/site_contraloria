# imagen oficial de pyhton mas compatible
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Comando por defecto (lo ajustaremos luego)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "contraloria_site.wsgi:application"]