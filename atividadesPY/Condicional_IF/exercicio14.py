# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

print("--Dias da Semana--")

diasem = input("Digite um número de 1 a 7: ")

if(diasem == '1'):
    print("Segunda-Feira")
elif(diasem =='2'):
    print("Terça-Feira")
elif(diasem == '3'):
    print("Quarta-Feira")
elif (diasem == '4'):
    print("Quinta-Feira")
elif(diasem == '5'):
    print("Sexta-Feira")
elif (diasem == '6'):
    print("Sábado")
elif(diasem == '7'):
    print("Domingo")