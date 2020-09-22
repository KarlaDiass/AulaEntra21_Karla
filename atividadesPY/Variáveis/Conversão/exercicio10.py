# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.


produto1 = input("Digite o nome do primeiro produto:")
qtd_produto1 = int(input("Quantas undidades você deseja?"))
preco_produto1 = float(input("Digite o preço do produto:"))

produto2 = input("Digite o nome do segundo produto:")
qtd_produto2 = int(input("Quantas unidades você deseja de?"))
preco_produto2 = float(input("Digite o preço do produto:"))

print(produto1,"você solicitou",qtd_produto1,"unidade(s). O valor total dessa compra é: R$", qtd_produto1 * preco_produto1)
print(produto2,"você solicitou",qtd_produto2,"unidade(s). O valor total dessa compra é: R$", qtd_produto2 * preco_produto2)