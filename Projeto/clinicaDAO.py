from pymongo import MongoClient
from bson.objectid import ObjectId
from entidades import *
from database import Database

db = Database(database = 'Clinica',collection = 'Animais')
data = db.collection.find()

#criar a classe que receberá a instância do objeto:
class ClinicaDAO(Animal):
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_animal(self, Animal):
        try:
            res = self.db.collection.insert_one({'_id': Animal.id, 'nome':Animal.nome, 'idade': Animal.idade, 'condição': Animal.condição, 'especie':Animal.especie, 'raça':Animal.raça, 'tutor':{'nome':Animal._tutor.nome,'idade':Animal._tutor.idade}, 'veterinario':{'nome':Animal._veterinario.nome,'crmv':Animal._veterinario.crmv}})
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao inserir este animal em nosso banco de dados: {e}")
            return None

    def read_animal(self, id: int):
        try:
            res = self.db.collection.find_one({"_id": id})
            print(f"Animal encontrado: {res}")
            return res
        except Exception as e:
            print(f"Um erro ocorreu ao procurar este animal. Tente novamente.: {e}")
            return None
        
    def read_condição(self, cond: str):
        try:
            res = list(self.db.collection.find({"condição": cond},{"nome":1,"idade":1}).sort("nome",1))
            print(f"Animal encontrado: {res}")
            return res
        except Exception as e:
            print(f"Um erro ocorreu na busca. Tente novamente.: {e}")
            return None
        
    def update_animal(self, id, nome_vet, crmv_vet, idade_animal, condicao_animal):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {'veterinario':{'nome':nome_vet,'crmv':crmv_vet}, 'idade': idade_animal, 'condição': condicao_animal}})
            print(f"Animal atualizado")
            return res.modified_count
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar esse animal. Tente novamente{e}")
            return None

    def delete_animal(self, id: int):
        try:
            res = self.db.collection.delete_one({"_id": id})
            print(f"Animal deletado!")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao realizar essa operação: {e}")
            return None