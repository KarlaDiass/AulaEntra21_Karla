#Execicios 01

#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%

comissao = float(input("Insira o valor da venda: "))

if(comissao >=0 and comissao <= 30000.00):
    print("Você não recebeu nenhuma porcentagem de comissão.")
elif(comissao >30000.00 and comissao<= 50000.00):
    valor_total = comissao*(1.5/100) 
    print("Você recebeu 1.5% de comissao, TOTAL DE: R$", valor_total)
elif(comissao > 50000.00 and comissao <= 100000.00):
    valor_total = comissao*(2.5/100) 
    print("Você recebeu 5.5% de comissao, TOTAL DE: R$", valor_total)
elif (comissao > 100000.00):
    valor_total = comissao*(3.5/100)
    print("Você recebeu 3.5% de comissao, TOTAL DE: R$", valor_total)