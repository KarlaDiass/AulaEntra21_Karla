# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.
print("Vamos Calcular o Delta!")
a = int(input("Digite o número de 'a':"))
b = int(input("Digite o número de 'b':"))
c = int(input("Digite o número de 'c':"))

delta = (b*b)-4*(a*c)

print("O resultado do Delta é igual a:", delta)
