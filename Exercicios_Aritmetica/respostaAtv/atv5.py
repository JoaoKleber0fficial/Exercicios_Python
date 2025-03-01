""" Atividade 5 """

""" 
Faça um programa que recebe um número em Pés, faça as conversões a seguir e
mostre os resultados.

Polegadas;
- Pes;
- Jardas;
- Milhas;

Sabe –se que:
1 Pé = 12 polegadas;
1 Jarda = 3 Pés;
1 Milha = 1.760 Jarda;
"""

""" RESPOSTA: """
polegadas = float(input('Coloque o valor desejado: '))
pes = polegadas / 12
jardas = pes / 3
milhas = jardas / 1760

print(f'Polegadas: {polegadas}')
print(f'Pés: {pes}')
print(f'Jardas: {jardas}')
print(f'Milhas: {milhas}')