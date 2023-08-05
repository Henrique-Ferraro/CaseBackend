import logging

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

def nome_nulo(nome):
    if nome == 0:
        logging.warning("O campo nome não pode ser vazio!!!")
    return (nome)

def sobrenome_nulo(sobrenome):
    if sobrenome == 0:
        logging.error("O campo sobrenome não pode ser nulo. Tente novamente.")
    return (sobrenome)


nome = nome_nulo()
logging.info(f"Nome: {nome}")

# lucro_acao = lucro_por_acoes(faturamento, custo, percentual_imposto, acoes)
# logging.info(f"Lucro por ação: {lucro_acao}")