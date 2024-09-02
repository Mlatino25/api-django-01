# Usa una imagen base que incluya las herramientas necesarias
FROM python:3.10-slim

# Instala dependencias del sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Copia el archivo de requisitos
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app

# Define el directorio de trabajo
WORKDIR /app

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
