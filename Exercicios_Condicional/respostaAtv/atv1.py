salario = input('Digite o salario: ')

novoSalario = float(salario)

conversaoSalario = float(0)

if float(salario) < 1000:

    conversaoSalario = float(salario) * 0.25

if float(salario) >= 1000 and float(salario) < 2000:

    conversaoSalario = float(salario) * 0.15

if float(salario) >= 2000:

    conversaoSalario = float(salario) * 0.10


print(novoSalario + conversaoSalario)
