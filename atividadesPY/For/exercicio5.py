"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""

print("--CADASTRAMENTO DE VENDAS DIÁRIAS--\n")

vendas_lista = []

qtt_vendas = int(input("Insira a quantidade de vendas que você realizou hoje:"))

for i in range(qtt_vendas):
    venda = float(input("Cadastre o valor da sua venda:"))
    vendas_lista.append(venda)
    media = sum(vendas_lista) / qtt_vendas 
print("\n")
print(f"QUANTIDADE DE VENDAS: {qtt_vendas};\nVALOR TOTAL: R${sum(vendas_lista)};\nMÉDIA DO DIA: R${media}")
