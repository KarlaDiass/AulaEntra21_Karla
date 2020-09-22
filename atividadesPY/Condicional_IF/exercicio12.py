# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

print(""" --CALCULADORA--

OPERAÇÕES:

Adição;
Subtração;
Multiplicação;
Divisão;
Potenciação;
""")

potencia = 0

opera = input("Digite a operação desejada: ")

if(opera == 'Adição'):
    num1 = int(input("Digite o primeiro número para adicionar: "))
    num2 = int(input("Digite o segundo número para adicionar: "))
    print("A adição dos dois números escolhidos é: ", num1+num2)

elif(opera == 'Subtração'):
    num1 = int(input("Digite o primeiro número para subtrair: "))
    num2 = int(input("Digite o segundo número para subtrair: "))
    print("A subtração dos dois números escolhidos é: ", num1-num2)

elif (opera == 'Multiplicação'):
    num1 = int(input("Digite o primeiro número para multiplicar: "))
    num2 = int(input("Digite o segundo número para multiplicar: "))
    print("A multiplicação dos dois números escolhidos é: ", num1*num2)

elif (opera == 'Divisão'):
    num1 = int(input("Digite o dividendo: "))
    num2 = int(input("Digite o divisor: "))
    print("O quociente dos dois números escolhidos é: ", num1/num2)

elif (opera == 'Potenciação'):
    num1 = int(input("Digite o número: "))
    num2 = int(input("Digite o expoente: "))
    print(num1, "elevado por",num2,"é igual a: ", num1**num2)    
    



