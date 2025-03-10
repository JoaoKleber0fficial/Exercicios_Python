
LimiteSpeed = 50.0

speedVeiculo = float(input('Qual é a velocidade que o veiculo passou: '))

listaMultas = [
    '00.00',
    '25.00',
    '40.00',
    '80.00'
]

if(speedVeiculo < LimiteSpeed):
    multa = listaMultas[0]
    print(f'Limite: {LimiteSpeed}km/h\n Velocidade: {speedVeiculo}\n Multa: R${multa}')

if(speedVeiculo >= LimiteSpeed):
    multa = listaMultas[1]
    print(f'Limite: {LimiteSpeed}km/h\n Velocidade: {speedVeiculo}\n Multa: R${multa}')

if(speedVeiculo >= (LimiteSpeed + 10)):
    multa = listaMultas[2]
    print(f'Limite: {LimiteSpeed}km/h\n Velocidade: {speedVeiculo}\n Multa: R${multa}')

if(speedVeiculo >= (LimiteSpeed + 20)):
    multa = listaMultas[3]
    print(f'Limite: {LimiteSpeed}km/h\n Velocidade: {speedVeiculo}\n Multa: R${multa}')