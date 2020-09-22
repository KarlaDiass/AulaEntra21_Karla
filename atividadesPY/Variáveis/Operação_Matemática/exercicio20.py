#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

dinheiro_emprestado = float(input("Informe o valor do dinheiro emprestado:"))
taxa_juros = float(input("Digite a taxa de juros: "))
tempo_emprestimo = int(input("Digite quantos meses deve durar o empréstimo: "))
valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print("O valor emprestado:", dinheiro_emprestado)
print("Taxa de juros:", taxa_juros,"%")
print("O valor recebido é:", valor_receber)