## Objetivos do projeto

1 - Requisitos funcionais
Desenvolver uma API onde seja possível receber dados pessoais e enviar uma notificação para aprovação.
Campos para os dados a serem recebidos na API:

a. Nome
b. Sobrenome
c. Idade
d. País

. Um método GET para consultar um cadastro
. Um método GET para listar todos os cadastros
. Um método POST para efetuar um cadastramento
. Um método PATCH para atualizar um dos dados do cadastro.
. Um método Delete para efetuar a exclusão do cadastro.

2 - Requisitos não funcionais obrigatórios:

– A API deve respeitar o padrão REST
– Deve possuir produzir logs.
– Uso de arquitetura hexagonal.
– A API deve utilizar solução conteinerizada.
– Devem ser implementados testes unitários com cobertura mínima de 90%.
– Todo código fonte deve estar em um repositório que fique acessível para avaliação.

3 - Requisitos não funcionais desejáveis:

– A aplicação, bem como a infra utilizada deve ser implementada através de Infra as Code
– Uso de AWS
– Uso de terraform
– Uso de orquestradores de containers - opcional
– A API deverá estar exposta em um API Gateway. - opcional

## Tecnologias utilizadas durante o projeto

* Python: v3.9.9
* Flask: v2.0.2
* Bootstrap: v5.1.x
* MySQL: v8.0.28
* mysql-connector-python: v8.0.28
* Flask-SQLAlchemy: v2.5.1
* Flask-WTF: v1.0.0
* Flask-Bcrypt: v0.7.1