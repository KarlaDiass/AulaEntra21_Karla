
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

print("--Solicitar compra de *Bolo de Chocolate*--")

nome = input("Digite seu nome:")
qtd_bolo = int(input("Digite a quantidade de bolos que você deseja:"))
preco = float(12.5)

print(nome, ", você solicitou a compra de:", qtd_bolo, "bolo(s) no valor de:",preco,"cada. O valor total da sua compra é igual a: R$", qtd_bolo * preco)

