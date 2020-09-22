# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
# 

num1 = int(input("Digite o primeiro número para a comparação: "))
num2 = int(input("Digite o segundo número: "))

if(num1>num2):
    print(num1, "é maior que",num2)
else:
    print(num2, "é maior que",num1)