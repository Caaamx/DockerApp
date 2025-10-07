FROM python:3.10-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear y establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY . .
COPY pages ./pages

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer puerto
EXPOSE 8501

# Comando para ejecutar la app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.port=8501", "--server.address=0.0.0.0"]