# https://docs.python.org/3/library/logging.html#logrecord-attributes

import logging

# Aqui definimos as configurações do modulo
logging.basicConfig(level=logging.INFO, 
                    filename="cadastro.log", 
                    filemode='a',
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Instancia do objeto getLogger()
logger = logging.getLogger('root')

def fullname(primeiro_nome: str, segundo_nome: str) -> str:
    """
        Essa função recebe o primeiro nome e o segundo nome de uma pessoa e retorna o nome completo dela.
    """

    # Aqui, verificamos se os parametros passados são do tipo string (str)
    if isinstance(primeiro_nome, str) and isinstance(segundo_nome, str):
        logger.info(f'{primeiro_nome} {segundo_nome}')
        return primeiro_nome + segundo_nome
    else:
        logger.error(
            f'{primeiro_nome} type: {type(primeiro_nome)} - {segundo_nome} type: {type(segundo_nome)}'
        )

fullname('Carlos', 'Alberto')
fullname('Rodrigo', True)

def fulldata(nome: str, sobrenome: str, idade: int, pais: str) -> str:
    """
        Essa função recebe todos os dados de uma pessoa e retorna os dados dela.
    """

    # Aqui, verificamos se os parametros passados são do tipo string (str)
    if isinstance(nome, str) and isinstance(sobrenome, str) and isinstance(idade, int) and isinstance(pais, str):
        logger.info(f'{nome} {sobrenome} {idade} {pais}')
        return nome + sobrenome + idade + pais
    else:
        logger.error(
            f'{nome} type: {type(nome)} - {sobrenome} - {idade} - {pais} type: {type(sobrenome)}'
        )

fullname('Carlos', 'Alberto')
fullname('Rodrigo', True)

fulldata('Carlos', 'Alberto', 'R43', True)
fulldata('Rodrigo', True, 45, 'Portugal')

# #### Resumo:
#
# logging.debug
# DEBUG - Informação detalhada, tipicamente de interesse apenas quando diagnosticando problemas.
#
# logging.info
# INFO - Confirmação de que as coisas estão funcionando como esperado.
#
# logging.warning
# WARNING - Uma indicação que algo inesperado aconteceu, ou um indicativo que algum problema em um futuro próximo (ex.: ‘pouco espaço em disco’). O software está ainda funcionando como esperado.
#
# logging.error
# ERROR - Por conta de um problema mais grave, o software não conseguiu executar alguma função.
#
# logging.critical
# CRITICAL - Um erro grave, indicando que o programa pode não conseguir continuar rodando.