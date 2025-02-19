n1 = float(input("Coloque a primeira nota do Aluno(a): "))
n2 = float(input("Coloque a segunda nota do Aluno(a): "))
n3 = float(input("Coloque a terceira nota do Aluno(a): "))
n4 = float(input("Coloque a quarta nota do Aluno(a): "))
n5 = float(input("Coloque a quinta nota do Aluno(a): "))

media = (n1 + n2 + n3 + n4 + n5) / 5.0

if media >= 0.0 and media <= 10.0:
    print(f'A média desse(a) aluno(a) é {media}')

else:
    print("Valores maior que 10.0 não são permitidos")