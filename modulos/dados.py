from modulos import interface
def cadastrarGasto(lista):
    novogasto = {}
    #id
    id = len(lista)
    novogasto['id'] = id
    #descricao
    while True:
        print()
        descricao = str(input('Descrição: ')).strip().title()
        if descricao == '':
            print(f'{interface.cores(1)}ERRO! Descrição em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Descrição "{descricao}" adicionada com sucesso!{interface.cores(9)}')
            novogasto['descricao'] = descricao
            break
    #valor
    while True:
        print()
        valor = str(input('Valor: R$')).replace(' ', '').replace(',', '.')
        if valor == '':
            print(f'{interface.cores(1)}ERRO! Valor em branco.{interface.cores(9)}')
            continue
        else:
            try:
                float(valor)
            except ValueError:
                print(f'{interface.cores(1)}ERRO! "R${valor.replace('.', ',')}" não é um número válido.{interface.cores(9)}')
                continue
            else:
                print(f'{interface.cores(2)}Valor "R${valor.replace('.', ',')}" adicionado com sucesso!{interface.cores(9)}')
                novogasto['valor'] = float(valor)
        break
    #categoria
    while True:
        print()
        categoria = str(input('Categoria: ')).strip().title()
        if categoria == '':
            print(f'{interface.cores(1)}ERRO! Categoria em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Categoria "{categoria}" adicionada com sucesso!{interface.cores(9)}')
            novogasto['categoria'] = categoria
            break
    #data -> criar uma validação para no caso de letras, do jeito que está o usuário pode adicionar letras nesse campo
    while True:
        print()
        data = str(input('Data [dd/mm/aaaa]: ')).replace(' ', '').replace('-', '/').replace('.', '/')
        if data == '':
            print(f'{interface.cores(1)}ERRO! Data em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Data "{data}" adicionada com sucesso!{interface.cores(9)}')
            novogasto['data'] = data
            break
    return novogasto


def deletarGasto(lista):
    while True:
        print()
        try:
            deletar = int(input('Qual o ID do gasto que você quer deletar? '))
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Digite apenas números inteiro.{interface.cores(9)}')
            print('Exemplo: "1"')
            continue
        else:
            if deletar >= len(lista) or deletar < 0:
                print(f'{interface.cores(1)}ERRO! ID inválido.{interface.cores(9)}')
                continue
            else:
                del lista[deletar]
                print(f'{interface.cores(2)}Gasto "#{deletar}" removido com sucesso!{interface.cores(9)}')
                break


def listarGastos(lista):
    if len(lista) == 0:
        print('Não há gastos cadastrados.')
        return
    else:
        for g in lista:
            print(f'ID: {g["id"]}')
            print(f'Descrição: {g["descricao"]}')
            print(f'Valor: R${g["valor"]:.2f}')
            print(f'Categoria: {g["categoria"]}')
            print(f'Data: {g["data"]}')
            print('-' * 30)


def totalCategoria(lista):
    if len(lista) == 0:
        print('Não há gastos cadastrados.')
        return
    else:
        totais = {}
        for g in lista:
            categoria = g['categoria']
            valor = g['valor']
            if categoria in totais:
                totais[f'{categoria}'] += valor
            else:
                totais[f'{categoria}'] = valor
        for k, v in totais.items():
            print(f'Categoria: {k} = {interface.cores(2)}R${v:.2f}{interface.cores(9)}'.replace('.', ','))
        return totais


def estatisticasGerais(lista):
    if len(lista) == 0:
        print('Não há gastos cadastrados.')
        return
    else:
        numgastos = len(lista)
        print(f'Número de gastos: {numgastos}')
        totalgastos = 0
        for g in lista:
            totalgastos += g['valor']
        print(f'Total dos gastos: {interface.cores(2)}R${totalgastos:.2f}{interface.cores(9)}'.replace('.', ','))
        mediagastos = totalgastos / numgastos
        print(f'Média dos gastos: {interface.cores(2)}R${mediagastos:.2f}{interface.cores(9)}'.replace('.', ','))
        descricaomai = ''
        mai = 0
        descricaomen = ''
        men = 0
        for g in range(0, len(lista)):
            if g == 0:
                descricaomai = lista[g]['descricao']
                mai = lista[g]['valor']
                descricaomen = lista[g]['descricao']
                men = lista[g]['valor']
            else:
                if lista[g]['valor'] > mai:
                    descricaomai = lista[g]['descricao']
                    mai = lista[g]['valor']
                elif lista[g]['valor'] < men:
                    descricaomen = lista[g]['descricao']
                    men = lista[g]['valor']
        print(f'O maior gasto é "{descricaomai}": {interface.cores(2)}R${mai:.2f}{interface.cores(9)}'.replace('.', ','))
        print(f'O menor gasto é "{descricaomen}": {interface.cores(2)}R${men:.2f}{interface.cores(9)}'.replace('.', ','))


def exportarDados(lista):
    if len(lista) == 0:
        print('Não há gastos cadastrados.')
        return
    else:
        with open('gastos.txt', 'w', encoding='utf-8') as arquivo:
            for gasto in lista:
                arquivo.write(f'Descrição: {gasto['descricao']}\n')
                arquivo.write(f'Valor: R${gasto['valor']:.2f}\n')
                arquivo.write(f'Categoria: {gasto['categoria']}\n')
                arquivo.write(f'Data: {gasto['data']}\n')
                arquivo.write('-' * 30 + '\n')
            print('Gastos exportados com sucesso para "gastos.txt"!')

