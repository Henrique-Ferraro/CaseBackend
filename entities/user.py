from pony.orm import PrimaryKey, Required, Set
from data.db import db

class Cadastro(db.Entity):
    _table_ = "user"
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    sobrenome = Required(str)
    idade = Required(int)
    pais = Required(str)