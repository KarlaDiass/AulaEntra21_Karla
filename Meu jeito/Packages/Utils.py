from sqlite3 import connect
from Packages.veiculos import Veiculos


def menu():
    return '''
------- Menu -------

1 - Cadastrar Pessoa
2 - Cadastrar veiculo
3 - Listar Pessoa
4 - Listar Veiculos
5 - Sair

> '''

def cadastro_veiculos(pessoas, lista:Veiculos):
    print("\n\t__________CADASTRO DE VEÍCULOS__________\n")
    nome = input('Nome do Carro: ').title()
    marca = input("Marca: ").title()
    modelo = input("Modelo: ").title()
    cor = input("Cor: ").title()
    placa = input("Placa: ").upper()
    print('Escolha um proprietario: ')
    # Tentar listar os usuarios
    proprietario = int(input('\n> '))
    num_portas = int(input("Número de portas: "))
    km_rodado = int(input("Km rodado: "))
    qtd_passageiros = int(input("Quantidade máxima de passageiros: "))
    ano = int(input("Ano: "))
    valor = int(input("Valor: R$ "))
    motor = float(input("Motor: "))
    combustivel = input("Tipo de combustível: ").title()
    meio_locomocao = input("Meio de locomoção: ").title()

    vaiculos = Veiculos(nome, marca, modelo, cor, placa, proprietario,\
           num_portas, km_rodado, qtd_passageiros, ano, valor,\
           motor, combustivel, meio_locomocao)
    lista = veiculos.lista 

    return lista 