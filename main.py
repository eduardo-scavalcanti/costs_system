from modulos import interface
from modulos import dados
from time import sleep
gastos = []
#titulo
interface.titulo('> CadasTrour V1.3 <')
#menu
while True:
    print()
    interface.opcaoMenu(1, 'Cadastrar gasto')
    interface.opcaoMenu(2, 'Editar gasto')
    interface.opcaoMenu(3, 'Deletar gasto')
    interface.opcaoMenu(4, 'Listar gastos')
    interface.opcaoMenu(5, 'Exibir total por categoria')
    interface.opcaoMenu(6, 'Estatísticas gerais')
    interface.opcaoMenu(7, 'Exportar dados')
    interface.opcaoMenu(0, 'Sair')
    print()
    try:
        opcao = int(input('Qual opção você deseja? '))
    except ValueError:
          print(f'{interface.cores(1)}ERRO! Digite apenas números inteiro.{interface.cores(9)}')
          print('Exemplo: "1"')
          continue
    else:
         if opcao < 0 or opcao > 7:
              print(f'{interface.cores(1)}ERRO! Opção inválida.{interface.cores(9)}')
    #opcao 1
    if opcao == 1:
        print()
        interface.titulo('> OPÇÃO 1 <')
        novogasto = dados.cadastrarGasto(gastos)
        gastos.append(novogasto.copy())
    #opcao 2
    elif opcao == 2:
         print()
         interface.titulo('> OPÇÃO 2 <')
         print()
         dados.editarGasto(gastos)
    #opcao 3
    elif opcao == 3:
         print()
         interface.titulo('> OPÇÃO 3 <')
         print()
         dados.deletarGasto(gastos)
         print()
    #opcao 4
    elif opcao == 4:
         print()
         interface.titulo('> OPÇÃO 4 <')
         print()
         dados.listarGastos(gastos)
    #opcao 5
    elif opcao == 5:
        print()
        interface.titulo('> OPÇÃO 5 <')
        print()
        dados.totalCategoria(gastos)
    #opcao 6
    elif opcao == 6:
         print()
         interface.titulo('> OPÇÃO 6 <')
         print()
         dados.estatisticasGerais(gastos)
    #opcao 7
    elif opcao == 7:
         print()
         interface.titulo('> OPÇÃO 7 <')
         print()
         print('Exportando gastos...')
         sleep(3)
         print()
         dados.exportarDados(gastos)
    #opcao 0
    if opcao == 0:
        print()
        interface.titulo('Saindo do programa...')
        sleep(3)
        break


# Resolver o valor que não aparece com 2 casas decimais na hora de editar o VALOR
