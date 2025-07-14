from modulos import interface
from modulos import dados
from time import sleep
gastos = []
#titulo
interface.titulo('> REGIX <')
sleep(1.5)
#nome
while True:
    print()
    nome = str(input('Olá! Digite o seu 1° nome: ')).strip().title()
    if nome == '':
        print(f'{interface.cores(1)}ERRO! Nome em branco.{interface.cores(9)}')
        continue
    else:
        print(f'Seja bem-vindo(a), {interface.cores(3)}{nome}{interface.cores(9)}.')
    sleep(1.5)
    break
#menu
while True:
    interface.titulo_com_espaco('> MENU <')
    interface.menu_principal()
    print()
    try:
        opcao = int(input('Qual opção você deseja? '))
    except ValueError:
          print(f'{interface.cores(1)}ERRO! O valor digitado não é válido.\nDigite apenas número inteiros.{interface.cores(9)}')
          continue
    else:
         if opcao < 0 or opcao > 7:
              print(f'{interface.cores(1)}ERRO! Opção inválida.{interface.cores(9)}')
    #opcao 1
    if opcao == 1:
        interface.titulo_com_espaco('> OPÇÃO 1 <')
        novogasto = dados.cadastrar_gasto(gastos)
        gastos.append(novogasto.copy())
    #opcao 2
    elif opcao == 2:
         interface.titulo_com_espaco('> OPÇÃO 2 <')
         dados.editar_gasto(gastos)
    #opcao 3
    elif opcao == 3:
         interface.titulo_com_espaco('> OPÇÃO 3 <')
         dados.deletar_gasto(gastos)
         print()
    #opcao 4
    elif opcao == 4:
         interface.titulo_com_espaco('> OPÇÃO 4 <')
         dados.listar_gastos(gastos)
    #opcao 5
    elif opcao == 5:
        interface.titulo_com_espaco('> OPÇÃO 5 <')
        dados.total_categorias(gastos)
    #opcao 6
    elif opcao == 6:
         interface.titulo_com_espaco('> OPÇÃO 6 <')
         dados.estatisticas_gerais(gastos)
    #opcao 7
    elif opcao == 7:
         interface.titulo_com_espaco('> OPÇÃO 7 <')
         print('Exportando gastos...')
         sleep(3)
         print()
         dados.exportar_dados(gastos)
    #opcao 0
    elif opcao == 0:
        interface.titulo_com_espaco('Saindo do programa...')
        sleep(1.5)
        print(f'Até a próxima, {interface.cores(3)}{nome}{interface.cores(9)}!')
        break

