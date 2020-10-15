#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

num = int(input('Insira um número para calcular a raiz: '))

def calc_raiz(indice):
    resultado = num ** (1/indice)
    return resultado

raiz = calc_raiz(3)
print(f'O resultado é: {raiz:.2f}')
