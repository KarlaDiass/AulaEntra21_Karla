n = int(input())

resto=0
hora = n//(60**2)
resto = n%(60**2)

minuto = resto//60
resto = resto - minuto*60

segundo = resto

print(f'{int(hora)}:{int(minuto)}:{int(segundo)}')