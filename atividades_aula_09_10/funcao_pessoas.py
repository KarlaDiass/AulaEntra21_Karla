pessoas = []
carac = '_'
lista_pessoas = []
def cadastrar_pessoa (nome, sobrenome, idade):
    pessoa = {}
    if(idade >= 18):
        pessoa['Nome'] = nome
        pessoa['Sobrenome'] = sobrenome
        pessoa['Idade'] = idade
        salvar_pessoas(pessoa)
        gerar_id(pessoa)
    else:
        printa('NÃO É POSSÍVEL CADASTRAR MENORES DE 18 ANOS')


def gerar_id(pessoa):
    arq_pessoas = open('atividades_aula_09_10/listagem_pessoas.txt', 'r')
    nCadastro = 0
    for contador in arq_pessoas:
        nCadastro = nCadastro + 1
    arq_pessoas.close()

    pessoa = {'ID':nCadastro}
    arqpessoas = open('atividades_aula_09_10/listagem_pessoas.txt', 'a')
    arqpessoas.write(f"{pessoa['ID']} \n")
    printa('PESSOA CADASTRADA COM SUCESSO')
    print(f"Seu ID é: {nCadastro}")
    arqpessoas.close()



def salvar_pessoas(pessoa):
    arquivo = open('atividades_aula_09_10/listagem_pessoas.txt','a')
    arquivo.write(f"{pessoa['Nome']};{pessoa['Sobrenome']};{pessoa['Idade']};")
    arquivo.close()
    


def listagem_pessoas():
    arquivo = open('atividades_aula_09_10/listagem_pessoas.txt','r')
    for linha in arquivo:
        linha_limpa = linha.strip() #-- limpa espaços em brando e caracteres de formatação (\n \t)
        pessoas = linha_limpa.split(';')
        print(f"\tNome: {pessoas[0]} - Sobrenome: {pessoas[1]} -  Idade: {pessoas[2]} - Id: {pessoas[3]}")
    arquivo.close()



def pessoas_especifica():
    n = input('\nDigite o ID da pessoa que você deseja verificar o cadastro: ')
    arq_pessoas = open('atividades_aula_09_10/listagem_pessoas.txt', 'r')

    for procura in arq_pessoas:
        linha_limpa = procura.strip()
        pessoas = linha_limpa.split(';')
        if (n == pessoas[3]):
            print(f"Nome: {pessoas[0]} - Sobrenome: {pessoas[1]} - Idade: {pessoas[2]} - Id: {pessoas[3]}")
        elif(n != pessoas[3]):
            printa('ID NÃO ENCONTRADO')
    arq_pessoas.close()



def cabecalho(titulo):
    print(f'{carac*20} {titulo} {carac*20}\n\n{carac*62}')

def printa(frase):
    print(f'\n{carac*10} {frase} {carac*10}')
