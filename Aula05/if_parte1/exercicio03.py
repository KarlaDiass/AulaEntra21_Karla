# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# 
# Caso contrário deve aparecer a mensagem "Entrada Negada!"

print("Entrada permitida somente para maiores de 18 anos!")

idade = int(input("Insira a sua idade: "))

if(idade>=18):
    print("Entrada permitida!")
else:
    print("Entrada negada!")