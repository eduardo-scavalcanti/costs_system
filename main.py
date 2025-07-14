from modulos import interface
from modulos import dados
from modulos import menu
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
              continue
    if opcao in menu.opcoes_menu:
         menu.opcoes_menu[opcao](gastos)
    elif opcao == 0:
        interface.titulo('Saindo do programa...')
        sleep(1.5)
        print(f'Até a próxima, {interface.cores(3)}{nome}{interface.cores(9)}!')
        break