
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 

print(""" 
--Receba um Elogio--

F = Feminino
M = Masculino
O = Outro
""")

gen = input("Insira o seu gênero: ")

if(gen == 'F'):
    print("Você é uma menina muito inteligente!")
elif (gen == 'M'):
    print("Como você está forte! Andou malhando?")
elif (gen == 'O'):
    print("Você é incrível!")
else:
    print("Opção Inválida")


