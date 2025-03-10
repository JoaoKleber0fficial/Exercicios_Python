nome = str(input('Escreva o nome da pessoa: '))

idade = int(input('Coloque a idade do usuario: '))

if idade <= 12 and idade > 0:
    print(f'{nome} é uma criança de {idade} anos')
elif idade >= 13 and idade <= 17:
    print(f'{nome} é um(a) adolescente de {idade} anos')
elif idade >= 18 and idade <= 59:
    print(f'{nome} é um(a) adulto(a) de {idade} anos')
elif idade >=60:
    print(f'{nome} é um(a) especialista de {idade} anos')

else:
    print('Não aceitamos numeros negativos tente novamente')