# Usa una imagen base de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el resto del código del proyecto a /app
COPY src/ /app

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
