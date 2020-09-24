n = int(input())

resto = 0

nota_cem = n/100

resto = n%100

nota_cinq = resto/50

resto = resto%50

nota_vint = resto/20

resto = resto%20

nota_dez = resto/10

resto = resto%10

nota_cin = resto/5

resto = resto%5

nota_dois = resto/2

resto = resto%2

nota_um = resto

print(n)
print(f'{int(nota_cem)} nota(s) de R$ 100,00')
print(f'{int(nota_cinq)} nota(s) de R$ 50,00')
print(f'{int(nota_vint)} nota(s) de R$ 20,00')
print(f'{int(nota_dez)} nota(s) de R$ 10,00')
print(f'{int(nota_cin)} nota(s) de R$ 5,00')
print(f'{int(nota_dois)} nota(s) de R$ 2,00')
print(f'{int(nota_um)} nota(s) de R$ 1,00')
