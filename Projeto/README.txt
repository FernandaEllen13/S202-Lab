#PROJETO PARA LABORATÓRIO DE BD II:

Este projeto trata-se de um banco de dados não-relacional de uma clínica veterinária, no qual 
o usuário poderá cadastrar, atualizar, buscar ou remover um paciente de seu banco. 

main -> rodará o Client(animalCLI) utilizando a construção de classes como modelo(clinicaDAO)

Veterinário: nome, crmv
Tutor: nome, idade
Animal: id,nome,idade,condição,especie,raça, atributos de veterinário e tutor
class Veterinario:
    def __init__(self,nome,crmv):
        self.nome = nome
        self.crmv = crmv

class Tutor:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Animal:
    def __init__(self, id, nome, idade, condição, especie, raça, _veterinario, _tutor):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.condição = condição
        self.especie = especie
        self.raça = raça
        self._veterinario = Veterinario()
        self._tutor = Tutor()

{
  "_id": 1,
  "nome": "Rogerio",
  "idade": 2,
  "condição": "FIV",
  "especie": "Gato",
  "raça": "SRD",
  "tutor":{"nome": "Fernanda","idade": 21},
  "veterinario":{"nome": "Claudia","crmv":112384}  
}