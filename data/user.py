from pony.orm import db_session
from pony.orm.core import ObjectNotFound
from data.base import base
from entities import user
from data.db import db
from collections import namedtuple

class user(base):
    def __init__(self):
        super().__init__(entity=user)
        self.base = base(user)

    @db_session
    def get_user(self, user_id):

        query = """
            SELECT *
            FROM caseBackend    
        """

        
        # Define a estrutura da linha de resultados como uma namedtuple
        ResultRow = namedtuple('ResultRow', ['id', 'nome', 'sobrenome', 'idade', 'pais'])
    
        # Executa a consulta SQL e obtém os resultados
        data = db.execute(sql=query, globals={"id": user_id}).fetchall()

        # Transforma os resultados em uma lista de dicionários
        result_list = [ResultRow(*row)._asdict() for row in data]

        return result_list
    
    def create_user(self, user: dict):
        entity_to_save = {
            "id": 1,
            "nome": user["nome"],
            "sobrenome": user["sobrenome"],
            "idade": user["idade"],
            "pais": user["pais"],
        }

        if not user.exists(id=user["id"], user_id=1):
            self.base.create(entity_to_save)

    @db_session
    def update_user(self, data: list[dict]):
        self.entity = user
        
        for user in data:
            id = user["id"]
            
            if id is None:
                self.create_user(user)
                continue
            
            try:
                user[id].set(id=user["id"])
            except ObjectNotFound:
                print("objeto com id %d não encontrado, tentando criar uma nova nome caso não exista" % id)
                self.create_user(user)

        return self.get_user(1)
    
    @db_session
    def delete_user(self, data: list[dict]):
        self.entity = user
        
        for user in data:
            id = user["id"]
            
            if id is None:
                self.delete_user(user)

        return self.get_user(1)
    
    