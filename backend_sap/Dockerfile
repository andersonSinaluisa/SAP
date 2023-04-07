# Imagen base de Python 3.7
FROM python:3.7

# Variables de entorno para la aplicación Django
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_ENV=production \
    PORT=8000 \
    WEB_CONCURRENCY=4 \
    DEBUG=False

RUN apt-get update && \
    apt-get install -y nginx && \
    rm /etc/nginx/sites-enabled/default && \
    pip install --upgrade pip  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Configurar directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivos requeridos
COPY ./requirements.txt /app/
COPY ./nginx.conf /etc/nginx/sites-enabled/def

# Instalar dependencias
RUN pip install -r requirements.txt || true

# Copiar el código fuente de la aplicación
COPY . /app/

# Ejecutar migraciones de Django


# Compilar archivos estáticos de Django

# Exponer el puerto 8000 para que Nginx pueda comunicarse con el contenedor
EXPOSE 8000

# Comando de arranque para el contenedor
ENTRYPOINT [ "sh", "/app/run.sh" ]
