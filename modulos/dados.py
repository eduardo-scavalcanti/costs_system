from modulos import interface
def nome():
    while True:
        nome = str(input('Olá! Digite o seu 1° nome: ')).strip().title()
        if nome == '':
            print(f'{interface.cores(1)}ERRO! Nome em branco.{interface.cores(9)}')
            continue
        else:
            print(f'Seja bem-vindo(a), {interface.cores(3)}{nome}{interface.cores(9)}.')
        return nome


def cadastrar_id(lista):
    id = len(lista)
    return id


def cadastrar_descricao():
    while True:
        descricao = str(input('Descrição: ')).strip().title()
        if descricao == '':
            print(f'{interface.cores(1)}ERRO! Descrição em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Descrição "{descricao}" adicionada com sucesso!{interface.cores(9)}')
            return descricao
            novogasto['descricao'] = descricao
            break


def cadastrar_valor():
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
                return valor


def cadastrar_categoria():
    while True:
        print()
        categoria = str(input('Categoria: ')).strip().title()
        if categoria == '':
            print(f'{interface.cores(1)}ERRO! Categoria em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Categoria "{categoria}" adicionada com sucesso!{interface.cores(9)}')
            return categoria


def cadastrar_data():
    #data -> criar uma validação para no caso de letras, do jeito que está o usuário pode adicionar letras nesse campo
    while True:
        print()
        dia = str(input('Dia [dd]: ')).replace(' ', '')
        try:
            int(dia)
        except:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(dia) < 1 or int(dia) > 31:
                print(f'{interface.cores(1)}ERRO! O dia "{dia}" não é válido.\nEscolha um dia entre 1 e 31.{interface.cores(9)}')
                continue
            else:
                print(f'{interface.cores(2)}Dia "{dia}" adicionado com sucesso!{interface.cores(9)}')
                break
    while True:
        print()
        mes = str(input('Mês [mm]: ')).replace(' ', '')
        try:
            int(mes)
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(mes) < 1 or int(mes) > 12:
                print(f'{interface.cores(1)}ERRO! O mês "{mes}" não é válido.\nEscolha um mês entre 1 e 12.{interface.cores(9)}')
                continue  
            else:
                print(f'{interface.cores(2)}Mês "{mes}" adicionado com sucesso!{interface.cores(9)}')
                break
    while True:
        print()
        ano = str(input('Ano [aaaa]: ')).replace(' ', '')
        try:
            int(ano)
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(ano) < 0:
                print(f'{interface.cores(1)}ERRO! O ano "{ano}" não é válido.\nEscolha um ano acima de 0.{interface.cores(9)}')
                continue
            else:
                print(f'{interface.cores(2)}Ano "{ano}" adicionado com sucesso!{interface.cores(9)}')
                break
    data = f'{dia}/{mes}/{ano}'
    print()
    print(f'{interface.cores(2)}Data "{data}" adicionado com sucesso!{interface.cores(9)}')
    return data


def cadastrar_gasto(lista):
    novogasto = {}
    id = cadastrar_id(lista)
    novogasto['id'] = id
    descricao = cadastrar_descricao()
    novogasto['descricao'] = descricao
    valor = cadastrar_valor()
    novogasto['valor'] = float(valor)
    categoria = cadastrar_categoria()
    novogasto['categoria'] = categoria
    data = cadastrar_data()
    novogasto ['data'] = data
    return novogasto


def editar_gasto(lista):
    while True:
        print()
        try:
            editar = int(input('Qual o ID do gasto que você quer editar? '))
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Digite apenas números inteiro.{interface.cores(9)}')
            print('Exemplo: "1"')
            continue
        else:
            if editar >= len(lista) or editar < 0:
                print(f'{interface.cores(1)}ERRO! ID inválido.{interface.cores(9)}')
                continue
            else:
                break
    #descricao
    while True:
        print()
        descricao = str(input('Descrição: ')).strip().title()
        if descricao == '':
            print(f'{interface.cores(1)}ERRO! Descrição em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Descrição "{lista[editar]['descricao']}" trocada por ', end='') 
            lista[editar]['descricao'] = descricao
            print(f'"{descricao}" com sucesso!{interface.cores(9)}')
            break
    #valor
    while True:
        print()
        valor = str(input('Valor: R$')).replace(' ', '').replace(',', '.')
        try:
            float(valor)
        except ValueError:
            print(f'{interface.cores(1)}ERRO! "R${valor.replace('.', ',')}" não é um número válido.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Valor "R${str(lista[editar]['valor']).replace('.', ',')}" trocado por ', end='')
            lista[editar]['valor'] = float(valor)
            print(f'"R${str(valor).replace('.', ',')}" com sucesso!{interface.cores(9)}')
            break
    #categoria
    while True:
        print()
        categoria = str(input('Categoria: ')).strip().title()
        if categoria == '':
            print(f'{interface.cores(1)}ERRO! Categoria em branco.{interface.cores(9)}')
            continue
        else:
            print(f'{interface.cores(2)}Categoria "{lista[editar]['categoria']}" trocada por ', end='')
            lista[editar]['categoria'] = categoria
            print(f'"{categoria}"" com sucesso!{interface.cores(9)}')
            break
    #data
    while True:
        print()
        dia = str(input('Dia [dd]: ')).replace(' ', '')
        try:
            int(dia)
        except:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(dia) < 1 or int(dia) > 31:
                print(f'{interface.cores(1)}ERRO! O dia "{dia}" não é válido.\n Escolha um dia entre 1 e 31.{interface.cores(9)}')
                continue
            else:
                print(f'{interface.cores(2)}Dia "{dia}" adicionado com sucesso!{interface.cores(9)}')
                break
    while True:
        print()
        mes = str(input('Mês [mm]: ')).replace(' ', '')
        try:
            int(mes)
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(mes) < 1 or int(mes) > 12:
                print(f'{interface.cores(1)}ERRO! O mês "{mes}" não é válido.\n Escolha um mês entre 1 e 12.{interface.cores(9)}')
                continue  
            else:
                print(f'{interface.cores(2)}Mês "{mes}" adicionado com sucesso!{interface.cores(9)}')
                break
    while True:
        print()
        ano = str(input('Ano [aaaa]: ')).replace(' ', '')
        try:
            int(ano)
        except ValueError:
            print(f'{interface.cores(1)}ERRO! Utilize apenas números inteiros.{interface.cores(9)}')
            continue
        else:
            if int(ano) < 0:
                print(f'{interface.cores(1)}ERRO! O ano "{ano}" não é válido.\n Escolha um ano acima de 0.{interface.cores(9)}')
                continue
            else:
                print(f'{interface.cores(2)}Ano "{ano}" adicionado com sucesso!{interface.cores(9)}')
                break
    data = f'{dia}/{mes}/{ano}'
    print()
    print(f'{interface.cores(2)}Data "{lista[editar]['data']}" trocada por ', end='')
    lista[editar]['data'] = data
    print(f'"{data}" com sucesso!{interface.cores(9)}')


def deletar_gasto(lista):
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
            if deletar < len(lista):
                for g in range(deletar, len(lista)):
                    lista[g]['id'] -= 1
                break
            else:
                break


def listar_gastos(lista):
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


def total_categorias(lista):
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


def estatisticas_gerais(lista):
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


def exportar_dados(lista):
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

