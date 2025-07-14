def cores(x):
    '''Adiciona cor ao texto.

    param "x": Valor relacionado a cor desejada.

    Número das cores:
    0 -> Branco
    1 -> Vermelho
    2 -> Verde
    3 -> Amarelo
    4 -> Azul
    5 -> Roxo
    6 -> Ciano
    7 -> Cinza
    9 -> Sem cor
    '''
    if x == 0: # -> Cinza
        return f'\033[0;30m' 
    elif x == 1: # -> Vermelho
        return f'\033[0;31m'
    elif x == 2: # -> Verde
        return f'\033[0;32m'
    elif x == 3: # -> Amarelo
        return f'\033[0;33m'
    elif x == 4: # -> Azul
        return f'\033[0;34m'
    elif x == 5: # -> Roxo
        return f'\033[0;35m'
    elif x == 6: # -> Ciano
        return f'\033[0;36m'
    elif x == 7: # -> Branco
        return f'\033[0;37m'
    elif x == 9: # -> Sem cor
        return f'\033[m'


def titulo(msg):
    print('-' * 40)
    print(msg.center(37))
    print('-' * 40)


def menu_principal():
    opcaoMenu(1, 'Cadastrar gasto')
    opcaoMenu(2, 'Editar gasto')
    opcaoMenu(3, 'Deletar gasto')
    opcaoMenu(4, 'Listar gastos')
    opcaoMenu(5, 'Exibir total por categoria')
    opcaoMenu(6, 'Estatísticas gerais')
    opcaoMenu(7, 'Exportar dados')
    opcaoMenu(0, 'Sair')


def opcaoMenu(x, msg):
    '''Adiciona uma linha personalizada para criação de menu, conta com esta estrutura:
    [número] -> texto

    param "x": número que será adicionado a linha
    param "msg": texto que será adicionado a linha
    '''
    print(f'{cores(0)}[{x}]{cores(9)} -> {cores(6)}{msg}{cores(9)}')
