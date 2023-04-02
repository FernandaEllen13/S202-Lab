from pymongo import MongoClient
import pprint

#abrindo conexão:
client = MongoClient('mongodb://localhost:27017')

#qual schema:
db = client['relatorio5']

#qual collection:
books = db.livros

#exibição do menu:
print('Selecione uma opcao:')
print('1- Inserir um novo documento')
print('2- Ver todos os documentos')
print('3- Atualizar um documento')
print('4- Remover um documento')

opc = input()

if opc == '1':
    id = int(input('ID do livro: '))
    titulo = input('Titulo do livro: ')
    autor = input('Autor do livro: ')
    ano = int(input("Ano do livro: "))
    preco = float(input('Preco do livro: '))
    #inserção do novo documento:
    newdoc = {
        "_id": id,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "preco": preco
    }
    result = db.livros.insert_one(newdoc)
    if result.acknowledged:
        print('Documento adicionado!')
    else:
        print('Erro ao adicionar documento!')

elif opc == '2':
    result = books.find()
    for aux in result:
        pprint.pprint(aux)

elif opc == '3':
    result = books.update_many(
        {"preco": {"$gt": 40}},
        {"$set": 39.99}
    )
    if result.acknowledged:
        print('Documento atualizado!')
    else:
        print('Erro ao atualizar documento!')

elif opc == '4':
    id = int(input("Digite o ID do livro que deseja remover:"))
    result = books.delete_one({"_id": id})
    if result.acknowledged:
        print('Documento removido!')
    else:
        print('Erro ao remover documento!')









