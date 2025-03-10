funcionario = input('Coloque o nome do funcionario(a): ')

while True:

    profissao = int(input('Coloque o numero da profissão do funcionario(a), numeros de 1-5: '))

    tabelaProfissoes = [
        '1: Matemático', '2: Analista de Sistemas',
        '3: Físico(a)', '4: Arquiteto(a)',
        '5: Piloto(a) de Aeronaves'
    ]

    tabelaProfissoes

    if(profissao == 1):
        profissao = 'matemático(a)'
        print(f'O funcionario(a) {funcionario} é um(a) {profissao}')
        break
    elif(profissao == 2):
        profissao = 'Analista de Sistemas'
        print(f'O funcionario(a) {funcionario} é um(a) {profissao}')
        break
    elif(profissao == 3):
        profissao = 'Físico(a)'
        print(f'O funcionario(a) {funcionario} é um(a) {profissao}')
        break
    elif(profissao == 4):
        profissao = 'Arquiteto(a)'
        print(f'O funcionario(a) {funcionario} é um(a) {profissao}')
        break
    elif(profissao == 5):
        profissao = 'Piloto(a) de Aeronaves'
        print(f'O funcionario(a) {funcionario} é um(a) {profissao}')
        break
    else:
        print('Coloque profissões existem, de 1-5')
        print(tabelaProfissoes)