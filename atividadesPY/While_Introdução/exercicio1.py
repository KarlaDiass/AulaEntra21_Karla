"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""

opcao = '' 

while opcao != 'S': 
    
    opcao = input('''
    ***CALCULADORA***

    1) Soma
    2) Subtração
    3) Multiplicação
    S) Sair

    Digite a opção desejada: ''')

    
  
    print('\n')
    if (opcao == '1'):
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        soma = num1 + num2
        print(f"O resultado da soma é: {soma}\n")
    elif (opcao == '2'):
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        sub = num1 - num2
        print(f"O resultado da subtração é: {sub}\n")
    elif (opcao == '3'):
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        mult = num1*num2
        print(f"O resultado da multiplicação é: {mult}")
    elif (opcao =='S'):
        print(f"Obrigada pela escolha\nATÉ!\n")
    else:
        print("Opção Invália")