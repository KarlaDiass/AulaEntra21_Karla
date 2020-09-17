"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

lista_nome = []
idade = 0

while (idade != ''):
    nome = str(input("Insira seu nome: "))

    if (nome != ''):
        idade = input("Insira sua idade: ")
        if not(idade): break
        if(int(idade) >= 18):
            print("Entrada Permitida\n")
            lista_nome.append(nome)
        else:
            print("Entrada Proíbida\n")      
    else:
        print("NOME EM BRANCO\n")

print("Obrigada pela preferência")   
print(f"""
Pessoas com a entrada permitida:
{lista_nome}
""")

