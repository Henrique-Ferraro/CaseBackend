import os

SECRET_KEY = 'caseBackend'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = '',
        senha = '',
        servidor = 'localhost',
        database = 'caseBackend'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'