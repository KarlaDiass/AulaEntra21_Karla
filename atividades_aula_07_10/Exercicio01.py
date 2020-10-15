#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

funcionario = {'nome': 'Daniel', 'sobrenome': 'Souza', 'cpf': '111.111.111-11', 'rg': '1.111.111', 'salario': 1000.00}

for chave, valor in funcionario.items():
    print(chave, '-', valor)
