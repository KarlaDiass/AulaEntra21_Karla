pessoas = []
carac = '_'
def cadastrar_pessoa (id_pessoa, nome, sobrenome, idade):
    pessoa = {}
    if(idade >= 18):
        pessoa['Nome'] = nome
        pessoa['Sobrenome'] = sobrenome
        pessoa['Idade'] = idade
        pessoas.append(pessoa)
        id_pessoa = len(pessoas)
        pessoa['Id_pessoa'] = id_pessoa 
        print(f'{carac*10} Pessoa cadastrada com sucesso {carac*10}')
        print(f'Seu ID é: {id_pessoa}')
        
    else:
        print ('\nNão é possível cadastrar pessoas menores de 18 anos')


def listagem_pessoas():
    for i in pessoas:
        print(i)


def pessoas_especifica():
    n = int(input('\nDigite o ID da pessoa que você deseja verificar o cadastro: '))
    n = n-1
    tam = len(pessoas) - 1
    if n < 0 or n > tam:
        print("\nID não encontrado!")
    else:
        print(pessoas[n])

def cabecalho(titulo):
    print(f'{carac*20} {titulo} {carac*20}\n\n{carac*62}')