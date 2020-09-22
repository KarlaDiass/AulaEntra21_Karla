"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro


ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""

print("_____CADASTRAMENTO DE CLIENTE_____\n")

qtt_clientes = int(input("INSIRA A QUANTIDADE DE CLIENTES PARA O CADASTRAMENTO: "))
lista_nome = []
lista_idade = []
lista_id = []


if(qtt_clientes >= 4):
    for i in range(qtt_clientes):
        nome = str(input("Inserir nome: "))
        idade = int(input("Inserir idade: "))
        id_ = i+1
        lista_nome.append(nome)
        lista_idade.append(idade)
        lista_id.append(id_)
else:
    print("\nNÃO É POSSÍVEL CADASTRAR MENOS DE 4 CLIENTES")

tamanho = len(lista_nome)

for i in range(tamanho):
    print(f"""
    ______________________________
    Dados do cliente cadastrado:
    ______________________________

    ID: {lista_id[i]}
    NOME: {lista_nome[i]}
    IDADE: {lista_idade[i]}""")
