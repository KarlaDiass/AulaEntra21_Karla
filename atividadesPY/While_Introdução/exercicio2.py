"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida" """

opcao = '' 

while opcao != 'S':   

    opcao = input('''
    --MENU--

    A) Soma
    B) Média de 4 números
    C) Tabuada
    S) Sair

    Digite a opção desejada: ''')
    print("\n")
    if (opcao == 'A'):
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        soma = num1 + num2
        print("\n")
        print(f"O resultado da soma é: {soma}")
    elif (opcao == 'B'):
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        num3 = int(input("Insira o terceiro número: "))
        num4 = int(input("Insira o quarto número: "))
        media = (num1 + num2 +num3 +num4)/4
        print("\n")
        print(f"A média dos quatro números inseridos é: {media}")
    elif (opcao == 'C'):
        num = int(input("Insira um número para realizar a tabuada: "))
        print("\n") 
        for i in range(10):
            print(f"{num} x {i+1} = {num*(i+1)}")
    elif (opcao == 'S'):
        print("Obrigada pela escolha!\nATÉ!\n")   
    else:
        print("Opção Inválida")
        