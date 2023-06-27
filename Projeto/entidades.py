class Veterinario:
    def __init__(self, nome, crmv):
        self.nome = nome
        self.crmv = crmv

class Tutor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Animal:
    def __init__(self, id, nome, idade, condição, especie, raça, _veterinario: Veterinario, _tutor: Tutor):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.condição = condição
        self.especie = especie
        self.raça = raça
        self._veterinario = _veterinario
        self._tutor = _tutor

