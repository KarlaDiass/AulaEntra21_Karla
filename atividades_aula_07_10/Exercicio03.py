#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

par1 = '''Eu podia muito bem ter perguntado: eu também mudo completamente dessa maneira? Não fomos escritos
para um único instrumento; eu não fui, nem você.'''
par2 = '''O que fui incapaz de identificar nessa promessa é que a frieza e a apatia encontram um jeito de anular
imediatamente quaisquer tréguas e resoluções assinadas em momentos ensolarados.'''

info = {'Título':'Me chame pelo seu nome', 'Edicao':'Digital 2018', 'Autor': 'André Aciman', 'Data de publicação':'18 de janeiro de 2018'}
print('\n')
for chave, valor in info.items():
    print(chave, '-', valor)

print('\n\t{}\n\t{}'.format(par1,par2))
