n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4*1))/10

if(media >= 7.0):
    print(f"Media: {media:.1f}\nAluno aprovado.")
elif(media < 5.0):
    print(f"Media: {media:.1f}\nAluno reprovado.")
elif(media >= 5.0) and (media <= 6.9):
    print(f"Media: {media:.1f}\nAluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media1 = (media + nota_exame)/2
    if(media1 >= 5.0):
        print("Aluno aprovado.")
    else:
        print('Aluno reprovado.')
    print(f'Média final: {media1:.1f}')

    
