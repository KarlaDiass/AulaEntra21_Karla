# Exercicio 4
# Escreva um programa que peça a nota de um aluno
# 
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# 
# Caso contrário deve aparecer a mensagem: "Reprovado"

print("--BOLETIM--")

nota = int(input("Digite a sua nota: "))

if(nota>=7):
    print("APROVADO(A)")
else:
    print("REPROVADO(A)")