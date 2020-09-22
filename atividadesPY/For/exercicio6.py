
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""

print("--LISTA DE CONVIDADOS DO CAMAROTE--\nLIMITE: 10 PESSOAS\n")

lista_convidados = []

for i in range(10):
    convidados = input("INSIRA O NOME COMPLETO: ")
    lista_convidados.append(convidados)

print("\n")
print("OS CONVIDADOS CADASTRADOS SÃO:")
for i in lista_convidados:
    print(i)