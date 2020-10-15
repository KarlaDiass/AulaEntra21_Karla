from funcao_pessoas import *

enderecos = []


def cadastro_endereco(ident, id_endereco, rua, numero, comp, bairro, cidade, estado):
    cadastro = {}
    if rua == '' or comp == '' or bairro == '' or cidade == '' or estado == '':
        print("\nPreencha todos os dados!!")
    else:
        if ident <= len(pessoas):
            cadastro['Rua: '] = rua
            cadastro['Numero: '] = numero
            cadastro['Complemento: '] = comp
            cadastro['Bairro: '] = bairro
            cadastro['Cidade: '] = cidade
            cadastro['Estado: '] = estado
            enderecos.append(cadastro)
            id_endereco = len(enderecos)
            cadastro['Id_endereco: '] = id_endereco
            print("\nEndereço Cadastrado com sucesso.")
        else:
            print("\nID não encontrada!")


def listagem_endereco():
    for i in enderecos:
        print(i)


def enderecos_especifico():
    ID = int(input("\nDigite o ID da pessoa que você deseja verificar o endereço: "))
    ID = ID-1
    tam = len(pessoas) - 1
    if ID < 0 or ID > tam:
        print("\nID não encontrado!")
    else:
        print(enderecos[ID])

