
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
alunos_nota= [ ] 

print("---VEJA SE VOCÊ PASSOU DE ANO---")

for i in range(10): 
    nota = float (input(f"Insira sua nota {i+1}: "))
    alunos_nota.append(nota)
    media = sum(alunos_nota) / len(alunos_nota)

if(media < 5.5):
    print(f"Você está REPROVADO(A)! Sua média é: {media}")
elif(media >= 5.5 and media < 7):
    print(f"Você está de RECUPERAÇÃO! Sua média é: {media}")
elif(media >= 7 and media <=10):
    print(f"Você está APROVADO(A)! Sua média é: {media}")