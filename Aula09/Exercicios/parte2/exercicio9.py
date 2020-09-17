
"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""
vendas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
maior_500 = []
menor_500 = []
for i in vendas:
    if (i<500):
        menor_500.append(i)
    elif(i>=500):
        maior_500.append(i)

print(f"LISTA 1: {menor_500};\nLISTA 2: {maior_500}\n")

print(f"O menor valor da lista 1 é: {min(menor_500)}. E o maior valor da lista 1 é: {max(menor_500)};\n")
print(f"O menor valor da lista 2 é: {min(maior_500)}. E o maior valor da lista 2 é: {max(maior_500)}")