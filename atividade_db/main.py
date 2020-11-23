from pessoas import Pessoa
from veiculos import cadastro_veiculos, Veiculo
import sqlite3


p = Pessoa(
    input('Digite algumas informações\nnome: '),
    input('CPF(11 digitos): '),
    int(input('Algumas informações sobre sua data de aniversario\ndia: ')),
    int(input('Mes: ')),
    int(input('Ano: ')),
    input('Voltando a mais algumas coisinhas...\nEndereco: '),
    float(input('Salario: ')),
    input('Profissao: '),
)
def listar_pessoas():
    bd = sqlite3.connect('pessoas.db')
    sql = bd.cursor()

    sql.execute('SELECT * FROM pessoas')

    print(sql.fetchall())

if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Pessoa
            2 - Cadastrar Veículo
            3 - Listar Pessoas
            4 - Listar Veículos
            5 - Sair\n"""))

        if valor == 1:
            print("cadastrar pessoa")
        elif valor == 2:
            cadastro_veiculos()
        elif valor == 3:
            listar_pessoas()
        elif valor == 4:
            listar_veiculos()
        elif valor == 5:
            print("Agradecemos a sua visita!")
            break
        else:
            print("Opção inválida!\n Tente novamente!")


