"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""

print("---CADASTRAMENTO DE CLIENTE---\n")
lista_nome = []
lista_gênero = []
lista_id = []
lista_idade = []

for i in range(5):
    nome = str(input("Inserir nome: "))
    gênero = str(input("Inserir gênero: "))
    idade = int(input("Inserir idade: "))
    id_ = i+1
    lista_nome.append(nome)
    lista_gênero.append(gênero)
    lista_idade.append(idade)
    lista_id.append(id_)

tamanho = len(lista_nome)

for i in range(tamanho):
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[i]}
    NOME: {lista_nome[i]}
    IDADE: {lista_idade[i]}
    GÊNERO: {lista_gênero[i]}
    """)

selecionar = int(input("Insira o ID do cliente que você deseja consultar: "))

if (selecionar == 1):
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[0]}
    NOME: {lista_nome[0]}
    IDADE: {lista_idade[0]}
    GÊNERO: {lista_gênero[0]}""")
    if (lista_idade[0] >=18 and lista_gênero[0] == 'Feminino'):
        print("Entrada Liberada, 50% de desconto no ingresso.")
    elif (lista_idade[0] >=18 and lista_gênero[0] == 'Masculino'):
        ("Entrada Liberada, 5% de desconto no ingresso.")
    elif(lista_idade[0] < 18):
        print("Entrada Proíbida.")

elif(selecionar == 2): 
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[1]}
    NOME: {lista_nome[1]}
    IDADE: {lista_idade[1]}
    GÊNERO: {lista_gênero[1]}""")
    if (lista_idade[1] >=18 and lista_gênero[1] == 'Feminino'):
        print("Entrada Liberada, 50% de desconto no ingresso.")
    elif (lista_idade[1] >=18 and lista_gênero[1] == 'Masculino'):
        ("Entrada Liberada, 5% de desconto no ingresso.")
    elif(lista_idade[1] < 18):
        print("Entrada Proíbida.")

elif(selecionar == 3): 
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[2]}
    NOME: {lista_nome[2]}
    IDADE: {lista_idade[2]}
    GÊNERO: {lista_gênero[2]}""")
    if (lista_idade[2] >=18 and lista_gênero[2] == 'Feminino'):
        print("Entrada Liberada, 50% de desconto no ingresso.")
    elif (lista_idade[2] >=18 and lista_gênero[2] == 'Masculino'):
        ("Entrada Liberada, 5% de desconto no ingresso.")
    elif(lista_idade[2] < 18):
        print("Entrada Proíbida.")

elif(selecionar == 4): 
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[3]}
    NOME: {lista_nome[3]}
    IDADE: {lista_idade[3]}
    GÊNERO: {lista_gênero[3]}""")
    if (lista_idade[3] >=18 and lista_gênero[3] == 'Feminino'):
        print("Entrada Liberada, 50% de desconto no ingresso.")
    elif (lista_idade[3] >=18 and lista_gênero[3] == 'Masculino'):
        ("Entrada Liberada, 5% de desconto no ingresso.")
    elif(lista_idade[3] < 18):
        print("Entrada Proíbida.")

elif(selecionar == 5): 
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[4]}
    NOME: {lista_nome[4]}
    IDADE: {lista_idade[4]}
    GÊNERO: {lista_gênero[4]}""")
    if (lista_idade[4] >=18 and lista_gênero[4] == 'Feminino'):
        print("Entrada Liberada, 50% de desconto no ingresso.")
    elif (lista_idade[4] >=18 and lista_gênero[4] == 'Masculino'):
        ("Entrada Liberada, 5% de desconto no ingresso.")
    elif(lista_idade[4] < 18):
        print("Entrada Proíbida.")

#professor, acho que meu código tá muito grande
#outra coisa, eu fui pela lógica que, se a pessoa é menor de idade, ela não precisa saber o quanto vai ganhar de desconto pois a entrada foi proibida