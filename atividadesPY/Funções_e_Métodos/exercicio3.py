# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
#
vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50, 750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00, 500.00]

media_armando = sum(vendas_armando) / len(vendas_armando)
media_eduardo = sum(vendas_eduardo) / len(vendas_eduardo)
media_paulo = sum(vendas_paulo) / len(vendas_paulo)

total_armando = sum(vendas_armando)
total_eduardo = sum(vendas_eduardo)
total_paulo = sum(vendas_paulo)

quant_armando = len(vendas_armando)
quant_eduardo = len(vendas_eduardo)
quant_paulo = len(vendas_paulo)

text = f"""MÉDIA DE VENDAS (ARMANDO): {media_armando}| VENDA TOTAL (ARMANDO): {total_armando}| QUANTIDADE DE VENDAS (ARMANDO): {quant_armando}\n 
MÉDIA DE VENDAS (EDUARDO): {media_eduardo}| VENDA TOTAL (EDUARDO): {total_eduardo}| QUANTIDADE DE VENDAS (EDUARDO): {quant_eduardo}\n
MÉDIA DE VENDAS (PAULO): {media_paulo}| VENDA TOTAL (PAULO): {total_paulo}| QUANTIDADE DE VENDAS (PAULO): {quant_paulo}"""

print(text)
print("\n")

print("Calculo de comissão de cada funcionário")
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
if(total_armando >= 0 and total_armando <= 1000.00 ):
    comissao_armando = total_armando * (1/100)
    print("O Armando recebeu 1% de comissão. TOTALIZANDO: R$",comissao_armando)
elif(total_armando > 1000 and total_armando <= 2500.00):
    comissao_armando = total_armando * (1.5/100)
    print("O Armando recebeu 1.5% de comissão. TOTALIZANDO: R$",comissao_armando)
elif(total_armando > 2500.00 and total_armando <= 5000):
    comissao_armando = total_armando * (2/100)
    print("O Armando recebeu 2% de comissão. TOTALIZANDO: R$",comissao_armando)
elif(total_armando > 5000.00):
    comissao_armando = total_armando * (3/100)
    print("O Armando recebeu 3% de comissão. TOTALIZANDO: R$",comissao_armando)

if(total_eduardo >= 0 and total_eduardo <= 1000.00 ):
    comissao_eduardo = total_eduardo * (1/100)
    print("O Eduardo recebeu 1% de comissão. TOTALIZANDO: R$",comissao_eduardo)
elif(total_eduardo > 1000 and total_eduardo <= 2500.00):
    comissao_eduardo = total_eduardo * (1.5/100)
    print("O Eduardo recebeu 1.5% de comissão. TOTALIZANDO: R$",comissao_eduardo)
elif(total_eduardo > 2500.00 and total_eduardo <= 5000):
    comissao_eduardo = total_eduardo * (2/100)
    print("O Eduardo recebeu 2% de comissão. TOTALIZANDO: R$",comissao_eduardo)
elif(total_eduardo > 5000.00):
    comissao_eduardo = total_eduardo * (3/100)
    print("O Eduardo recebeu 3% de comissão. TOTALIZANDO: R$",comissao_eduardo)

if(total_paulo >= 0 and total_paulo <= 1000.00 ):
    comissao_paulo = total_paulo * (1/100)
    print("O Paulo recebeu 1% de comissão. TOTALIZANDO: R$",comissao_paulo)
elif(total_paulo > 1000 and total_paulo <= 2500.00):
    comissao_paulo = total_paulo * (1.5/100)
    print("O Paulo recebeu 1.5% de comissão. TOTALIZANDO: R$",comissao_paulo)
elif(total_paulo > 2500.00 and total_paulo <= 5000):
    comissao_paulo = total_paulo * (2/100)
    print("O Paulo recebeu 2% de comissão. TOTALIZANDO: R$",comissao_paulo)
elif(total_paulo > 5000.00):
    comissao_paulo = total_paulo * (3/100)
    print("O Paulo recebeu 3% de comissão. TOTALIZANDO: R$",comissao_paulo)