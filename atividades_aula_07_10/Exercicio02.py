#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

menu = {1 : 'Cadastrar Funcionário', 2 : 'Listar Funcionários', 3 : 'Editar Funcionários', 4 : 'Deletar Funcionário', 5 : 'Sair'}

print("_____SISTEMA DE CADASTRAMENTO DE FUNCIONÁRIOS_____\n\n")
for chave, valor in menu.items():
    print('\t',chave,'-', valor)

opcao = int(input("\n\nInsira um número de acordo com o que você deseja: "))

if(opcao == 1):
    print("\n\t___Cadastro de Funcionário:___\n\n\n\t*corpo*\n\n\t_____")
elif(opcao == 2):
    print("\n\t___Lista dos Funcionários Cadastrados:___\n\n\n\t*corpo*\n\n\t_____")
elif(opcao == 3):
    print("\n\t___Editar Dados dos Funcionários:___\n\n\n\t*corpo*\n\n\t_____")
elif(opcao == 4):
    print("\n\t___Excluir Funcionário:___\n\n\n\t*corpo*\n\n\t_____")
elif(opcao == 5):
    print("\n\t______\n\n\n\tSaindo...\n\n\t______")
    









