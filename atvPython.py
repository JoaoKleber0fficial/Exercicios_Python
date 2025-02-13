media = 0
notas = 0

for nota in range(1, 6):
    nota = float(input(f"Digite a {nota}ª nota: "))

    notas = notas + nota

    media = notas / 5

print(f'Sua média é {media}')