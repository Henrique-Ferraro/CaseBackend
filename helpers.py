import os
from main import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioCadastro(FlaskForm):
    nome = StringField('Nome', [validators.DataRequired(), validators.Length(min=1, max=50)])
    sobrenome = StringField('Sobrenome', [validators.DataRequired(), validators.Length(min=1, max=40)])
    idade = StringField('Idade', [validators.DataRequired(), validators.Length(min=1, max=20)])
    pais = StringField('País', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
