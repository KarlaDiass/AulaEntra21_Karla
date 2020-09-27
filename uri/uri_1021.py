nota, moeda = (input().split("."))

nota = int(nota)
moeda = int(moeda)

nota_cem = nota//100
resto = nota%100

nota_cinq = resto//50
resto = resto%50

nota_vint = resto//20
resto = resto%20

nota_dez = resto//10
resto = resto%10

nota_cin = resto//5
resto = resto%5

nota_dois = resto//2
resto = resto%2

moeda_umreal = resto//1

moeda_cinq = moeda//50
resto = moeda%50

moeda_vcinc = resto//25
resto = resto%25

moeda_dez = resto//10
resto = resto%10

moeda_cinc = resto//5
resto = resto%5

moeda_um = resto
print("NOTAS:")
print(f'{int(nota_cem)} nota(s) de R$ 100.00')
print(f'{int(nota_cinq)} nota(s) de R$ 50.00')
print(f'{int(nota_vint)} nota(s) de R$ 20.00')
print(f'{int(nota_dez)} nota(s) de R$ 10.00')
print(f'{int(nota_cin)} nota(s) de R$ 5.00')
print(f'{int(nota_dois)} nota(s) de R$ 2.00')
print("MOEDAS:")
print(f'{int(moeda_umreal)} moeda(s) de R$ 1.00')
print(f'{int(moeda_cinq)} moeda(s) de R$ 0.50')
print(f'{int(moeda_vcinc)} moeda(s) de R$ 0.25')
print(f'{int(moeda_dez)} moeda(s) de R$ 0.10')
print(f'{int(moeda_cinc)} moeda(s) de R$ 0.05')
print(f'{int(moeda_um)} moeda(s) de R$ 0.01')