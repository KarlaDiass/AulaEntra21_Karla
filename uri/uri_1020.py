n = int(input())

ano = n/365
resto = n%365

mes = resto/30
dia = resto%30

print(f'{int(ano)} ano(s)')
print(f'{int(mes)} mes(es)')
print(f'{int(dia)} dia(s)')