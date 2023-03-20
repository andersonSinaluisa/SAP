# Imagen base para construir la aplicación de Django
FROM python:3.9-slim-buster AS django

# Variables de entorno para MySQL
ENV MYSQL_DATABASE=dbname \
    MYSQL_USER=user \
    MYSQL_PASSWORD=password \
    MYSQL_HOST=db \
    MYSQL_PORT=3306

# Instala dependencias
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Crea directorio de trabajo
RUN mkdir /app
WORKDIR /app

# Copia archivos de la aplicación
COPY requirements.txt /app/
COPY . /app/

# Instala dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para migrar la base de datos
RUN python manage.py migrate --no-input

# Configura los archivos estáticos
RUN python manage.py collectstatic --no-input

# Imagen base para construir el servidor Nginx
FROM nginx:1.21-alpine

# Copia la configuración de Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copia los archivos estáticos de la aplicación de Django
COPY --from=django /app/static /usr/share/nginx/html

# Expone el puerto de la aplicación
EXPOSE 80

# Comando de inicio de Nginx
CMD ["nginx", "-g", "daemon off;"]
