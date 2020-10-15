from funcao_pessoas import *

from funcao_enderecos import *

cabecalho('CADASTRO DE CLIENTES')

escolha = 'S'
 
while escolha == 'S':

    nome = input('\nInsira seu nome: ')
    sobrenome = input('\nInsira seu sobrenome: ')
    idade = int(input('\nInsira sua idade: '))
    id_pessoa = None

    cadastrar_pessoa(id_pessoa, nome, sobrenome, idade)
    escolha = input("\nDeseja cadastrar uma nova pesssoa? S/N: ").upper()
    
if escolha == 'N':
    while escolha == 'N':
        ident = int(input("\nDigite sua ID para cadastro de endereço: "))

        rua = input("\nInforme o nome da rua: ")
        numero = int(input("\nDigite o número da sua casa: "))
        comp = input("\nInforme o complemento do endereço: ")
        bairro = input("\nInforme o bairro: ")
        cidade = input("\nInforme a cidade: ")
        estado = input("\nInforme o estado: ")

        cadastro_endereco(ident, id_pessoa, rua, numero, comp, bairro, cidade, estado)
       
        escolha = input("\nVocê terminou de cadastrar os endereços? S/N: ").upper()
        
if escolha == 'S':
    while escolha == 'S':
        pessoas_especifica()
        escolha = input('\nVocê deseja verificar o cadastro de mais alguém? S/N: ').upper() 

if escolha == 'N':
    while escolha == 'N':
        enderecos_especifico()
        escolha = input('\nVocê terminou de verificar os endereços? S/N: ').upper()

print("\n_____Lista de todas as pessoas cadastradas_____")
print('\n')
listagem_pessoas()
print("\n_____Lista de todos os endereços cadastrados_____")
print('\n')
listagem_endereco()


