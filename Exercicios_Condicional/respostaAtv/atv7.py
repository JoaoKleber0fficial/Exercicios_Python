tabelaIMC = {
    '1': 'Magreza',
    '2': 'Magreza',
    '3': 'Magreza',
    '4': 'Magreza',
    '5': 'Magreza',
}

peso = float(input('Digite o seu peso: '))

altura = float(input('Digite sua altura: ')) 

imc = peso / (altura ** 2)

if imc < 18.0:
    print(f"Você está abaixo do peso ideal: {imc}")

if imc >= 18.0 and imc <= 24.9:
    print(f"Você está no peso ideal: {imc}")

if imc >= 25.0 and imc <= 28.9:
    print(f"Você está com sobrepeso: {imc}")

if imc >= 30:
    print(f"Você está muito a cima do peso ideal: {imc}")