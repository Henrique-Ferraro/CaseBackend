from models.models import Cadastro
import pytest

class TestClass:
    def test_quando_nome_recebe_nome1_deve_retornar_nome(self):
        entrada = 'Roberto Alves' # Given-Contexto
        esperado = 'Roberto'

        nome_teste = Cadastro('Roberto Alves', entrada, 35, 'Brasil')
        resultado = nome_teste.nome() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_sobrenome1_deve_retornar_sobrenome(self):
        entrada = 'Roberto Alves' # Given-Contexto
        esperado = 'Alves'

        sobrenome_teste = Cadastro('Roberto Alves', entrada, 35, 'Brasil')
        resultado = sobrenome_teste.sobrenome() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_idade_recebe_idade1_deve_retornar_idade(self):
        entrada = 35 # Given-Contexto
        esperado = 35

        idade_teste = Cadastro('Roberto Alves', entrada, 35, 'Brasil')
        resultado = idade_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_pais_recebe_pais1_deve_retornar_pais(self):
        entrada = 'Brasil' # Given-Contexto
        esperado = 'Brasil'

        pais_teste = Cadastro('Roberto Alves', entrada, 35, 'Brasil')
        resultado = pais_teste.pais() # When-ação

        assert resultado == esperado  # Then-desfecho