import os
import platform  # Import the platform module to detect the operating system

from utils import *

lista_inscritos = [] 
conexao_base(lista_inscritos)

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')  # On Windows, use 'cls' to clear the screen
    else:
        os.system('clear')  # On non-Windows systems, use 'clear'

while True:
    clear_screen()
    print('MENU')
    print('1 - Fazer inscrições')
    print('2 - Listar inscritos')
    print('3 - Registrar entrada')
    print('4 - Registrar saída')
    print('5 - Finalizar')
    op = input('\nOpção: ')

    if op == '1':
        clear_screen()
        print('\nInscrições')
        inscricao(lista_inscritos)
    elif op == '2':
        clear_screen()
        print('Listagem de inscritos')
        listagem(lista_inscritos)
    elif op == '3':
        clear_screen()
        print('Registrar entrada')
        entrada(lista_inscritos)
    elif op == '4':
        clear_screen()
        print('Registrar saída')
        saida(lista_inscritos)
    elif op == '5':
        break
    else:
        clear_screen()
        print('Opção inválida!')

    input('Pressione Enter para continuar...')

clear_screen()
