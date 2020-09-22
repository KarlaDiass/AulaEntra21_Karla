# Exercicio 16
# Foi verificado que a venda de bermudas aumenta conforme aumenta a temperatura (t) (float) conforme a seguinte fórmula:
# 
# bermudas = 1.5t + t + 150
# 
# Lembrando que o t significa temperatura.
# 
# Faça um programa para o seu superior que peça a temperatura e mostre a venda prevista de bermudas.

print("--Venda das bermudas--")
t = float(input("Digite a temperatura:"))

venda_prevista = (1.5 * t) + t + 150

print("A venda prevista de bermuda é igual a:", venda_prevista)
