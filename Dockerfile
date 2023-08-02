FROM flask:python3.8
FROM flask

# Espaço de trabalho
WORKDIR /app

RUN pip install flask_swagger_ui
RUN pip install flask
RUN pip install -r requirements.txt

# Copia para dentro do container
COPY . .

CMD ["python", "src/app.py"]