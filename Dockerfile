FROM flask:python3.8
FROM flask

# Espaço de trabalho
WORKDIR /main

RUN pip install flask
RUN pip install -r requirements.txt
RUN pip install Flask: v2.0.2
RUN pip install Bootstrap: v5.1.x
RUN pip install MySQL: v8.0.28
RUN pip install mysql-connector-python: v8.0.28
RUN pip install Flask-SQLAlchemy: v2.5.1
RUN pip install Flask-WTF: v1.0.0
RUN pip install Flask-Bcrypt: v0.7.1

# Copia para dentro do container
COPY . .

CMD ["python", "main.py"]