from app.utils import clear_screen
from app.modules.routes.view import RoutesView


class MenuView:
    def show():
        option = None

        while option != '3':
            if option in [None, '4']:
                clear_screen()

                print('======================\n'
                    '         Menu\n'
                    '======================\n'
                    '  1. Cadastrar rotas\n'
                    '  2. Consultar rotas\n'
                    '  3. Sair\n'
                    '======================\n')

            option = input(
                'Qual operação deseja realizar' + (
                    ' [4 - Retornar ao menu]' if option not in [None, '1', '2', '3', '4'] else ''
                ) + '? '
            )

            if option == '1':
                RoutesView.create()
                option = None

            elif option == '2':
                RoutesView.read()
                option = None

            elif option not in ['3', '4']:
                print('Opção inválida, por favor, tente novamente...\n')
