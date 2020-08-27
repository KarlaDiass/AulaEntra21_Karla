# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.


print("--Descubra o menor número--")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))


if(num1<num2 and num1<num3):
    print(num1,"é o menor")
else:
    if(num2<num1 and num2<num3):
        print(num2,"é o menor")
    else:
        print(num3,"é o menor")

