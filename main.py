from modulos import interface, dados, menu
from time import sleep
gastos = []
#titulo
interface.titulo('> REGIX <')
sleep(1.5)
#nome
nome = dados.nome()
sleep(1.5)
#menu
while True:
    interface.titulo('> MENU <')
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
    if opcao == 1:
        menu.executar_opcao_1(gastos)
    elif opcao == 2:
        menu.executar_opcao_2(gastos)
    elif opcao == 3:
        menu.executar_opcao_3(gastos)
    elif opcao == 4:
        menu.executar_opcao_4(gastos)
    elif opcao == 5:
        menu.executar_opcao_5(gastos)
    elif opcao == 6:
        menu.executar_opcao_6(gastos)
    elif opcao == 7:
        menu.executar_opcao_7(gastos)
    elif opcao == 0:
        interface.titulo('Saindo do programa...')
        sleep(1.5)
        print(f'Até a próxima, {interface.cores(3)}{nome}{interface.cores(9)}!')
        break

