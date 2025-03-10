lanches = {
    '1': 'Big Mac',
    '2': 'Quarteirão',
    '3': 'McChicken',
    '4': 'Cheddar McMelt',
    '5': 'Mc Max'
}

print(f'Possiveis lanches\n {lanches}')

pedido = str(input('Escolha o numero de acordo com o pedido de 1-5: '))

for lanche in lanches:

    if int(pedido) > 0 and int(pedido) < 6:
        if lanche == pedido:
            print(f'Esse foi o seu pedido: {lanches[lanche]}')
    else:
        print('Pedido não encontrado')