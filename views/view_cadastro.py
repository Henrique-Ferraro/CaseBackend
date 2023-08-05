from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app, db
from models.models import Cadastro
from helpers import FormularioCadastro


@app.route('/')
def index():
    lista = Cadastro.query.order_by(Cadastro.id)
    return render_template('lista.html', titulo='Cadastro', cadastros=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioCadastro()
    return render_template('novo.html', titulo='Novo Cadastro', form=form)

@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioCadastro(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data
    sobrenome = form.sobrenome.data
    idade = form.idade.data
    pais = form.pais.data

    cadastro = Cadastro.query.filter_by(nome=nome).first()

    if cadastro:
        flash('Cadastro já existente!')
        return redirect(url_for('index'))

    novo_cadastro = Cadastro(nome=nome, sobrenome=sobrenome, idade=idade, pais=pais)
    db.session.add(novo_cadastro)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    cadastro = Cadastro.query.filter_by(id=id).first()
    form = FormularioCadastro()
    form.nome.data = cadastro.nome
    form.sobrenome.data = Cadastro.sobrenome
    form.idade.data = Cadastro.idade
    form.pais.data = Cadastro.pais
    
    return render_template('editar.html', titulo='Editando Cadastro', id=id, form=form)

@app.route('/atualizar', methods=['PATCH',])
def atualizar():
    form = FormularioCadastro(request.form)

    if form.validate_on_submit():
        Cadastro = Cadastro.query.filter_by(id=request.form['id']).first()
        Cadastro.nome = form.nome.data
        Cadastro.sobrenome = form.sobrenome.data
        Cadastro.idade = form.idade.data
        Cadastro.pais = form.pais.data

        db.session.add(Cadastro)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>', methods=['DELETE',])
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Cadastro.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Cadastro deletado com sucesso!')

    return redirect(url_for('index'))
