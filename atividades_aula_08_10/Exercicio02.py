#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

def calc_divisao():
    num1 = float(input('Insira o dividendo: '))
    num2 = float(input('Insira o divisor: '))
    if(num2 == 0):
        print('Impossível Calcular')
    else:
        divisao = num1/num2
        print(f'A divisão de {num1} por {num2} é igual a: {divisao}')
    
calc_divisao()
