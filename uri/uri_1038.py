cod, qtt = map(int, input().split())

preco = [4.00, 4.50, 5.00, 2.00, 1.50]

total = preco[cod-1]*qtt
print(f"Total: R$ {total:.2f}")