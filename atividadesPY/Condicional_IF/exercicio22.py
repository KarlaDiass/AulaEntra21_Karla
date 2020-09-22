"""Execicios 03

Escreva um programa que contenha um menu com 4 opções:
A) soma
B) média
C) divisão
D) Sair

As opções podem ser escolhidas com as letras maiusculas ou minusculas.

Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
"""

print("""--SOLICITE A AÇÃO DESEJADA--\n

SOMAR    DIVIDIR    MÉDIA

SAIR
""")

solicitar = input("Insira aqui: ")

if(solicitar == 'Somar' or solicitar == 'somar' or solicitar == 'SOMAR'):
    num1 = int(input("Digite o primeiro número para a soma: "))
    num2 = int(input("Digite o segundo número para a soma: "))
    print("A soma dos dois números inseridos é igual a: ",num1+num2)
elif(solicitar == 'Dividir' or solicitar == 'dividir' or solicitar == 'DIVIDIR'):
    num1 = int(input("Digite o dividendo: "))
    num2 = int(input("Digite o divisor: "))
    if(num2 == 0):
        print("Erro! Não pode dividir por ZERO!")
    else:
        print("A divisão dos dois números é igual a: ", num1/num2)
elif (solicitar == 'média' or solicitar == 'Média' or solicitar == 'MÉDIA'):
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))
    valor4 = int(input("Digite o quarto valor: "))
    media = (valor1+valor2+valor3+valor4)/4
    print("A média é igual a: ", media)
elif(solicitar == 'Sair' or solicitar == 'sair' or solicitar == 'SAIR'):
    print("Muito Obrigado e Volte sempre!")
