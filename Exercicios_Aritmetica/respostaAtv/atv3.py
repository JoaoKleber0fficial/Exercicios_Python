""" Atividade 3 """

""" 
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
salário, sabendo-se que este sofreu um aumento de 25%.
"""

""" RESPOSTA: """
salario = float(input("Digite o salario atual do funcionario(a): "))

salarioAumento = salario + (salario * 0.25)

print(f'Esse é o salario antes do aumento: R$ {salario}')
print(f'Esse é o salario pos aumento: $ {salarioAumento}')