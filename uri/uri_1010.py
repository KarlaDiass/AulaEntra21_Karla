cod1, qtt1, valor1 = (input().split())
cod2, qtt2, valor2 = (input().split())

total = (int(qtt1) * float(valor1)) + (int(qtt2) * float(valor2))

print(f'VALOR A PAGAR: R$ {total:.2f}')
