"""Execicios 02

Escreva um programa que receba 4 notas e calcule a média.
Mostre a seguinte mensagem conforme a media final.

Media Final
de 0 a 5 - Reprovado
de 5 a 6.5 - Recuperação
de 6.5 a 9 - Aprovado
Acima de 9 - Aprovado com louvor
"""
print("--BOLETIM--\n")


nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

if(media == 0 and media <= 5):
    print("Sua média é: \n", media, "REPROVADO(A)")
elif(media > 5 and media <6.5):
    print("Sua média é: \n", media,"RECUPERAÇÃO")
elif(media >= 6.5 and media < 9):
    print("Sua média é: \n", media,"APROVADO(A)")
elif(media >=9):
    print("Sua média é: \n", media,"APROVADO(A) COM LOUVOR")