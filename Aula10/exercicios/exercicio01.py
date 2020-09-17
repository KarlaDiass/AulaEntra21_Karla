"""
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:



***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
"""
print("---CADASTRAMENTO DE CLIENTE---\n")
lista_nome = []
lista_gênero = []
lista_tel = []

for i in range(5):
    nome = str(input("Insira seu nome: "))
    lista_nome.append(nome)
    gênero = str(input("Insira seu gênero: "))
    lista_gênero.append(gênero)
    tel = int(input("Insira seu número de telefone: "))
    lista_tel.append(tel)


tamanho = len(lista_nome)
for i in range(tamanho):
    print(f"""
    ***********************************
    Relatório de clientes cadastrados 
    ***********************************
    Nome: {lista_nome[i]}
    Gênero: {lista_gênero[i]}
    Telefone: {lista_tel[i]}
    """)
