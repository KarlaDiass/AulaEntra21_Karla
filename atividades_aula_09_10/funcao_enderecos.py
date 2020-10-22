from funcao_pessoas import *

enderecos = []


def cadastro_endereco(ident, rua, numero, comp, bairro, cidade, estado):
    cadastro = {}
    if rua == '' or comp == '' or bairro == '' or cidade == '' or estado == '':
        print("\nPreencha todos os dados!!")

    else:
        cadastro['Id_pessoa'] = ident
        cadastro['Rua'] = rua
        cadastro['Número'] = numero
        cadastro['Complemento'] = comp
        cadastro['Bairro'] = bairro
        cadastro['Cidade'] = cidade
        cadastro['Estado'] = estado
        salvar_endereco(cadastro)
        print("\nEndereço Cadastrado com sucesso.")
   

     
def salvar_endereco(cadastro):
    enderecos.append(cadastro)
    arquivo = open('atividades_aula_09_10/listagem_enderecos.txt','a')
    arquivo.write(f"{cadastro['Id_pessoa']};{cadastro['Rua']};{cadastro['Número']};{cadastro['Complemento']};{cadastro['Bairro']};{cadastro['Cidade']};{cadastro['Estado']}\n")
    arquivo.close()


def listagem_endereco():
    arquivo = open('atividades_aula_09_10/listagem_enderecos.txt','r')
    for linha in arquivo:
        linha_limpa = linha.strip()
        lista_end = linha_limpa.split(';')
        print(f"\tId_pessoa: {lista_end[0]} - Rua: {lista_end[1]} - Número da casa: {lista_end[2]} - Complemento: {lista_end[3]} - Bairro: {lista_end[4]} - Cidade: {lista_end[5]} - Estado: {lista_end[6]}")
    arquivo.close()


def enderecos_especifico():
    ID = input("\nDigite o ID da pessoa que você deseja verificar o endereço: ")
    arq_enderecos = open('atividades_aula_09_10/listagem_enderecos.txt', 'r')

    for procura in arq_enderecos:
        linha_limpa = procura.strip()
        enderecos = linha_limpa.split(';')
        if (ID == enderecos[0]):
            print(f"Id_pessoa: {enderecos[0]} - Rua: {enderecos[1]} - Número da casa: {enderecos[2]} - Complemento: {enderecos[3]} - Bairro: {enderecos[4]} - Cidade: {enderecos[5]} - Estado: {enderecos[6]}")
        elif(ID != enderecos[0]):
            printa('ID NÃO ENCONTRADO')
    arq_enderecos.close()


