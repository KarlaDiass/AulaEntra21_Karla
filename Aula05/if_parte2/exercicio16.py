# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 

print("""PROMOÇÃO DE COMBUSTÍVEL--

- Para  Gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto

- Para Diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto

- para Álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto
""")

tipo_combus = input("Insira o tipo de combústivel desejado: ")
litros = int(input("Insira quantos litros você deseja: "))

if(tipo_combus == 'Gasolina'):
    if(litros <= 20):
        print("Você não ganhou desconto na Gasolina")
    else:
        print("Você ganhou 10% de desconto na Gasolina!")
elif(tipo_combus == 'Diessel'):
    if(litros <= 10):
        print("Você ganhou 1.5% de desconto no seu Diessel!")
    else:
        print("Você ganhou 5% de desconto no seu Diessel")
elif(tipo_combus == 'Álcool'):
    if(litros <= 10):
        print("Você ganhou 5% de desconto no Álcool!")
    else:
        print("Você ganhou 10% de desconto no Álcool!")