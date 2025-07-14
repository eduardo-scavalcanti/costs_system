import interface, dados
def executar_opcao_1(lista_gastos):
    interface.titulo('> OPÇÃO 1 <')
    novogasto = dados.cadastrar_gasto(lista_gastos)
    lista_gastos.append(novogasto.copy())


def executar_opcao_2(lista_gastos):
    interface.titulo('> OPÇÃO 2 <')
    dados.editar_gasto(lista_gastos)


def executar_opcao_3(lista_gastos):
    interface.titulo('> OPÇÃO 3 <')
    dados.deletar_gasto(lista_gastos)


def executar_opcao_4(lista_gastos):
    interface.titulo('> OPÇÃO 4 <')
    dados.listar_gastos(lista_gastos)


def executar_opcao_5(lista_gastos):
    interface.titulo('> OPÇÃO 5 <')
    dados.total_categorias(lista_gastos)


def executar_opcao_6(lista_gastos):
    interface.titulo('> OPÇÃO 6 <')
    dados.estatisticas_gerais(lista_gastos)


def executar_opcao_7(lista_gastos):
    interface.titulo('> OPÇÃO 7 <')
    print('Exportando gastos...')
    dados.exportar_dados(lista_gastos)

