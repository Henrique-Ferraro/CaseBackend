import logging

logging.basicConfig(level=logging.INFO, filename="cadastro.log", format="%(asctime)s - %(levelname)s - %(message)s")

def nome_nulo(nome):
    if nome == 0:
        logging.warning("O campo nome não pode ser vazio!!!")
    return (nome)

def sobrenome_nulo(sobrenome):
    if sobrenome == 0:
        logging.error("O campo sobrenome não pode ser nulo. Tente novamente.")
    return (sobrenome)

def idade_nulo(idade):
    if idade != 0:
        logging.info("O campo idade realizado com sucesso!!")
    return (idade)

def pais_nulo(pais):
    if pais == 0:
        logging.debug("O campo pais não pode ser numeros.")
    return (pais)

def todos_nulo(todos):
    if todos == 0:
        logging.critical("Todos os campos devem ser preencidos.")
    return (todos)



nome = nome_nulo()
logging.info(f"Nome: {nome}")

sobrenome = sobrenome_nulo()
logging.info(f"Sobrenome: {sobrenome}")

idade = idade_nulo()
logging.info(f"idade: {idade}")

pais = pais_nulo()
logging.info(f"pais: {pais}")

todos = todos_nulo()
logging.info(f"todos: {todos}")