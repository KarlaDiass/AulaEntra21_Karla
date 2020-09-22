# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
print("--APROVADO OU REPROVADO?--")


nota1 = int(input("Insira sua primeira nota: "))
nota2 = int(input("Insira sua segunda nota: "))
nota3 = int(input("Insira sua terceira nota: "))
nota4 = int(input("Insira sua quarta nota: "))

media = (nota1 + nota2 + nota3 +nota4)/4

if(media == 10):
    print("MÉDIA:", media,"APROVADO(A) COM LOUVOR")
elif (media >= 7):
    print("MÉDIA:",media,"APROVADO(A)")
elif (media < 7):
    print("MÉDIA:", media,"REPROVADO(A)")