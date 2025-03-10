numeroMes = str(input("Digite o numero do mês que você deseja: "))

meses = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abrio',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}

for mes in meses:
    if mes == numeroMes:
        print(f'O mês que você selecionou foi o mês de {meses[mes]}')