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
    interface.opcaoMenu(2, 'Listar gastos')
    interface.opcaoMenu(3, 'Exibir total por categoria')
    interface.opcaoMenu(4, 'Estatísticas gerais')
    interface.opcaoMenu(5, 'Exportar dados')
    interface.opcaoMenu(0, 'Sair')
#opcao -> limitar o input para 0 a 5 (está aceitando outros números)
    print()
    try:
        opcao = int(input('Qual opção você deseja? '))
    except ValueError:
          print(f'{interface.cores(1)}ERRO! Digite apenas números inteiro.{interface.cores(9)}')
          print('Exemplo: "1"')
          continue
#opcao 1
    if opcao == 1:
        print()
        interface.titulo('> OPÇÃO 1 <')
        novogasto = dados.cadastrarGasto()
        gastos.append(novogasto.copy())
#opcao 2
    elif opcao == 2:
         print()
         interface.titulo('> OPÇÃO 2 <')
         print()
         dados.listarGastos(gastos)
#opcao 3
    elif opcao == 3:
        print()
        interface.titulo('> OPÇÃO 3 <')
        print()
        dados.totalCategoria(gastos)
#opcao 4
    elif opcao == 4:
         print()
         interface.titulo('> OPÇÃO 4 <')
         print()
         dados.estatisticasGerais(gastos)
#opcao 5
    elif opcao == 5:
         print()
         interface.titulo('> OPÇÃO 5 <')
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



#CRUD -> Create, read, update e delete (funções básicas que a maioria dos sistemas tem) (editar, deletar)
#ID -> Adicionar um ID para cada gasto para o CRUD
#