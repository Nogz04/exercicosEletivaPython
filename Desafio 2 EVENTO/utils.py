import os
from datetime import datetime

def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat', 'r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0].strip())
        leitor.close()
    except FileNotFoundError:
        open('inscricoes.dat', 'w').close()
    except Exception as e:
        print(f"Erro ao ler a base de dados: {str(e)}")

def inscricao(lista):
    matricula = input('\nInforme matrícula: ')
    matricula = matricula.strip()
    if matricula in lista:
        print('\nEsta matrícula já foi inscrita no evento')
    else:
        lista.append(matricula)
        nome = input('Nome: ')
        nome = nome.upper()
        email = input('Email: ')
        email = email.lower()
        escritor = open('inscricoes.dat', 'a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def listagem(lista):
    try:
        leitor = open('inscricoes.dat', 'r', encoding='utf8')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('Nome:', vetor_linha[1], 'Matrícula:', vetor_linha[0])
        leitor.close()
    except FileNotFoundError:
        print('\nSem inscrições até o momento')
    except Exception as e:
        print(f"Erro ao listar inscrições: {str(e)}")

def registrar_entrada(matricula, nome, email):
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('entradas_saidas.log', 'a') as log_file:
        log_file.write(f'Entrada: Matrícula {matricula}, Nome: {nome}, Email: {email}, Data e Hora: {data_hora}\n')

def registrar_saida(matricula, nome, email):
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('entradas_saidas.log', 'a') as log_file:
        log_file.write(f'Saída: Matrícula {matricula}, Nome: {nome}, Email: {email}, Data e Hora: {data_hora}\n')

def entrada(lista):
    matricula = input('Digite a matrícula do inscrito para registrar a entrada: ')
    matricula = matricula.strip()
    if matricula in lista:
        for linha in open('inscricoes.dat', 'r', encoding='utf8'):
            vetor_linha = linha.split(';')
            if vetor_linha[0] == matricula:
                nome = vetor_linha[1]
                email = vetor_linha[2]
                print(f'Entrada registrada para a matrícula {matricula}')
                registrar_entrada(matricula, nome, email)
                break
    else:
        print('\nMatrícula não encontrada')

def saida(lista):
    matricula = input('\nDigite a matrícula do inscrito para registrar a saída: ')
    matricula = matricula.strip()
    if matricula in lista:
        for linha in open('inscricoes.dat', 'r', encoding='utf8'):
            vetor_linha = linha.split(';')
            if vetor_linha[0] == matricula:
                nome = vetor_linha[1]
                email = vetor_linha[2]
                print(f'Saída registrada para a matrícula {matricula}')
                registrar_saida(matricula, nome, email)
                break
    else:
        print('Matrícula não encontrada')
