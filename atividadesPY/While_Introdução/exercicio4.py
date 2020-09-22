"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair
 
-----



Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""

lista_nome = []
lista_idade = []
lista_sexo = []
lista_tel = []

opcao = '' 


while (opcao != 'S'):
    opcao = input(f"""
    Cadastro de pessoas 

    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados
    C) Ver cadastro pelo nome
    D) Apagar um cadastro pelo nome
    S) Sair

    Insira a opção desejada: 
    """)

    if(opcao == 'A'):
        print("Cadastrar pessoa:\n")
        
        lista_nome.append(input("\nInserir nome: "))
        lista_idade.append(input("\nInserir idade: "))
        lista_sexo.append(input("\nInserir sexo (F ou M): "))
        lista_tel.append(input("\nInserir número de telefone: "))
            
    elif (opcao == 'B'):
        print(f"""Nome das pessoas cadastradas:
        {lista_nome}""")
        
    elif (opcao == 'C'):
        dados = input("Insira o nome do cliente que você deseja ver os dados: ")
        qtt = len(lista_nome)   
        print(qtt)
        for i in range(qtt):
            if ( lista_nome[i] == dados): 
                print(f"""
                Nome: {lista_nome[i]}
                Idade: {lista_idade[i]}
                Sexo: {lista_sexo[i]}
                Telefone: {lista_tel[i]}
                """)

    elif (opcao == 'D'):
        excluir = input("Insira o nome do cliente que você deseja excluir os dados: ")
        qtt = len(lista_nome)
        for i in range(qtt):
            if( lista_nome[i] == excluir):
                del(lista_nome[i])
                del(lista_idade[i])
                del(lista_sexo[i])
                del(lista_tel[i])
        print("DADOS EXCLUÍDOS")
    elif(opcao == 'S'):
        print("\nObrigada pela preferência\nATÉ!\n")
    
    else:
        print("Opção Inválida")



        

