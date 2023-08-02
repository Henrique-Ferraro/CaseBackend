FROM python:3
FROM flask

# Espaço de trabalho
WORKDIR /app

RUN "/requirements.txt"

# Copia para dentro do container
COPY . .

CMD ["python", "src/app.py"]