# Establecer la imagen base
FROM python:3.10.10-alpine

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar el archivo requirements.txt a la imagen
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# RUN python manage.py migrate

# Copiar los archivos de la aplicación a la imagen
COPY . .

# Exponer el puerto que se utilizará para la aplicación
EXPOSE 8000

# Ejecutar los comandos para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]