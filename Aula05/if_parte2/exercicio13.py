# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

print("--CADASTRO--")

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
endereço = input("Insira seu endereço: ")
email = input("Insira seu email: ")
tel = input("Insira seu número de telefone: ")

print("""--Selecione o que deseja consulatar--

Dados   Endereço    Contato""")

escolha = input("Insira a sua escolha aqui: ")

if(escolha == 'Dados'):
    print(nome,"\n",idade,"anos")
elif(escolha == 'Endereço'):
    print(endereço)
elif(escolha == 'Contato'):
    print(email,"\n",tel)




