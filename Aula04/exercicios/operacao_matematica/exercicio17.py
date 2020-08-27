# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 
print("Calculadora de área de uma circunferência")

r = float(input("Insira o valor do raio (em metros) da cincunferência:"))

area = 3.14 * (r * r)

print("A área da sua circunferência é igual a:",area, "m²")