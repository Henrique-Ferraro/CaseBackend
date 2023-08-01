# Instalar o Flask - pip install flask
# Flask - É o servidor
# jsonify - para retornar um no formato Json
# request - para acessar os dados que estao indo para a requisição

from flask import Flask, jsonify, request

# Criando uma aplicação Flask com o nome do arquivo app
app = Flask(__name__)

#Criação da fonte de dados, onde serão armazenados os cadastros

cadastros = [
    {
        'id': 1,
        'Nome': 'Henrique',
        'Sobrenome': 'Ferraro',
        'Idade': 37,
        'País': 'Brasil',
    },
    {
        'id': 2,
        'Nome': 'João',
        'Sobrenome': 'Silveira',
        'Idade': 21,
        'País': 'Portugal',
    },
    {
        'id': 3,
        'Nome': 'John',
        'Sobrenome': 'Shimth',
        'Idade': 45,
        'País': 'Austrália',
    },
]


# Realiza a consulta de todos os cadastros

@app.route('/cadastros', methods=['GET']) # endpoint
def obter_cadastro():
    return jsonify(cadastros)

# Realiza a consulta do cadastro por Id

@app.route('/cadastros/<int:id>', methods=['GET']) # endpoint
def obter_cadastro_id(id):
    for cadastro in cadastros:
        if cadastro.get('id') == id:
            return jsonify(cadastro)

# Realiza a edição do cadastro por Id

@app.route('/cadastros/<int:id>', methods=['PATCH']) # endpoint
def editar_cadastro_id(id):
    cadastro_alterado = request.get_json()
    for indice, cadastro in enumerate (cadastros):
        if cadastro.get('id') == id:
            cadastros[indice].update(cadastro_alterado)
            return jsonify(cadastros[indice])

# Realiza a criação do cadastro

@app.route('/cadastros', methods=['POST']) # endpoint
def incluir_cadastro():
    novo_cadastro = request.get_json()
    cadastros.append(novo_cadastro)
    return jsonify(cadastros)

# Exclui um cadastro

@app.route('/cadastros<int:id>', methods=['DELETE']) # endpoint
def excluir_cadastro(id):
    for indice, cadastro in enumerate(cadastros):
        if cadastro.get('id') == id:
            del cadastros[indice]
    return jsonify(cadastros)


app.run(port = 5000, host = 'localhost', debug = True)