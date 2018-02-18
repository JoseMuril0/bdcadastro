from dml import db_insert, db_delete, db_update, db_select, db_select_total
from pprint import pprint
import os

def menu ():
    print('+------------------------------------------+')
    print('|             SYSYEM-MENU                  |')
    print('+------------------------------------------+')
    print('| 1 - Cadastra-se                          |')
    print('| 2 - Editar                               |')
    print('| 3 - Deletar cadastro                     |')
    print('| 4 - Busca por email                      |')
    print('| 5 - Busca completa                       |')
    print('| 6 - Sair do sistema                      |')
    print('+------------------------------------------+')
# inicio main:
user = 0
while user != 6:
    menu()
    user = int(input('Deseja realizar algo? '))
    if (user == 1):
        ide = int(input('ID: '))
        nome = input('NOME: ')
        telefone = input('TELEFONE: ')
        email = input('EMAIL: ')
        db_insert(ide, nome, telefone, email)
        os.system('pause')
        os.system('cls')
    elif user == 2:
        novoNome = input('NOVO NOME: ')
        email = input('EMAIL CORRESPONDETE: ')
        db_update(novoNome, email)
        os.system('pause')
        os.system('cls')
    elif user == 3:
        email = input('EMAIL A SER EXCLUIDO: ')
        db_delete(email)
        os.system('pause')
        os.system('cls')
    elif user == 4:
        email = input('BUSCA EMAIL: ')
        db_select(email)
        os.system('pause')
        os.system('cls')
    elif user == 5:
        db_select_total()
        os.system('pause')
        os.system('cls')
    elif user == 6:
        os.system('pause')
        os.system('cls')

os.system('pause')
os.system('cls')
