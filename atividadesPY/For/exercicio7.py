"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""

print("""EM COMEMORAÇÃO AO ANIVERSÁRIO DE 100 ANOS DO SHOPPING,
VOCÊ PODE RECEBER GRATUITAMENTE UM INGRESSO PARA UM EVENTO DE ACORDO COM A SUA IDADE!!!

PARA RECEBER O PRESENTE VOCÊ SÓ PRECISA CADASTRAR A SUA IDADE ABAIXO!

APROVEITE!!!\n """)

lista_idade = []


for i in range(10):
    idade = int(input("INSIRA A SUA IDADE: "))
    lista_idade.append(idade)

for i in lista_idade:
    if(i<13):
        print(f"{i} anos. INGRESSO PARA A PISCINA DE BOLINHAS LIBERADO")
    elif(i>=13 and i<16):
        print(f"{i} anos. INGRESSO PARA O FLIPERAMA LIBERADO ")
    elif(i>=16 and i<18):
        print(f"{i} anos. INGRESSO PARA O CINEMA LIBERADO")
    elif(i>18):
        print(f"{i} anos. INGRESSO PARA A RAVE LIBERADO")