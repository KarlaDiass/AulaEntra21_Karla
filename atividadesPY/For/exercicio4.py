"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
listaNome = []
listaIdade = []
listaEmail = []

for i in range(10):
    nome = str(input("Insira seu nome:"))
    listaNome.append(nome)
    idade = int(input("Insira sua idade:"))
    listaIdade.append(idade)
    email = str(input("Insira seu email:"))
    listaEmail.append(email)
print("\n")
print(f"NOME: {listaNome}\nIDADE: {listaIdade}\nE-MAIL: {listaEmail}\n")
    