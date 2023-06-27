from database import Database
from entidades import *
from clinicaDAO import ClinicaDAO

db = Database(database='Clinica', collection='Animais')
data = db.collection.find()
clinica = ClinicaDAO(db)


aux = True

while(aux):
    print('Bem vindo ao Banco de Dados da Clínica do Dr. Rogerio! Digite o comando que deseja: inserir, buscar, buscar_condição, atualizar ou remover:')
    comando = input('Entre com um comando: ')
    
    if comando == 'inserir':
        print('\n--- Inserindo animal ---')
        print('Insira o numero de identificação do animal: ')
        animal_id = int(input())
        print('Insira o nome do animal: ')
        animal_nome = input()
        print('Insira sua idade: ')
        animal_idade = int(input())
        print('Insira qual sua condição médica: ')
        animal_condição = input()
        print('Insira qual sua espécie: ')
        animal_especie = input()
        print('Insira qual sua raça: ')
        animal_raça = input()

        print('--- Inserindo tutor ---')
        print('Digite seu nome: ')
        tutor_nome = input()
        print('Digite sua idade: ')
        tutor_idade = int(input())
        print('-----------------------------------------------------')
        print('Processo de inserção do tutor encerrado!')

        print('\n---Inserindo veterinário---')
        #print('Digite o número de identificação do veterinário do animal: ')
        #veterinario_id = input()
        print('Digite seu nome: ')
        vet_nome = input()
        print('Digite seu CRMV: ')
        vet_crmv = int(input())
        print('-----------------------------------------------------')
        print('Processo de inserção do tutor encerrado!')

        


        
        # Atribuindo as info ao obj
        tutor = Tutor(tutor_nome,tutor_idade)
        vet = Veterinario(vet_nome,vet_crmv)
        animal = Animal(animal_id,animal_nome,animal_idade,animal_condição,animal_especie,animal_raça,vet,tutor)
        
        # Chamando a função 
        clinica.create_animal(animal)
        
    elif comando == 'buscar':
        print('Digite o ID do animal que deseja ver: ')
        id = int(input())
        clinica.read_animal(id)

    elif comando == 'buscar_condição':
        print('Digite a condição dos animais que deseja buscar: ')
        cond: str
        cond =input()
        clinica.read_condição(cond)
    
    elif comando == 'atualizar':
        print('Digite o ID do animal que deseja atualizar seu cadastro: ')
        id = int(input())
        print('Nome do veterinário atual: ')
        novo_nome_vet = input()
        print('CRMV do veterinário atual: ')
        novo_crmv_vet = int(input())
        print('Atualizar estado de saúde: ')
        nova_condicao = input()
        print('Atualizar idade: ')
        novo_animal_idade = int(input())

        clinica.update_animal(id,novo_nome_vet,novo_crmv_vet,novo_animal_idade,nova_condicao)
        
        
    elif comando == 'remover':
        print('Digite o ID do animal que deseja remover de nosso banco de dados: ')
        id = int(input())
        clinica.delete_animal(id)
        
    elif comando == 'sair':
        print('Você saiu!')
        aux = False
    
    else:
        print('Comando invalido. Tente novamente.')