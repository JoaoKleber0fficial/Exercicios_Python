lado1 = int(input('Me informe o 1° Lado: '))
lado2 = int(input('Me informe o 2° Lado: '))
lado3 = int(input('Me informe o 3° Lado: '))

if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print(f'É um triangulo Equilátero de 3 lados iguais: {lado1}cm, {lado2}cm e {lado3}cm')

if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print(f'É um triangulo Escaleno de 3 lados diferentes: {lado1}cm, {lado2}cm e {lado3}cm')
    
if lado1 == lado2 and lado2 != lado3 or lado2 == lado3 and lado1 != lado3 or lado1 == lado3  and lado1 != lado2 :
    print(f'É um triangulo Isósceles de 2 lados iguais: {lado1}cm, {lado2}cm e {lado3}cm')

