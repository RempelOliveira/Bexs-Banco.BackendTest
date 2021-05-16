from app.utils import clear_screen, format_price
from app.modules.routes.controller import RoutesController, RouteController


class RoutesView:
    def create():
        clear_screen()

        print('\n======================\n'
              '        Rotas\n'
              '======================\n'
              '  Rotas devem ser casdatradas no seguinte formato: \n\n'
              '  Conexões: GRU - BRC - SCL\n'
              '     Preço: 40.00\n'
              '======================\n')

        connections = input('Insira os códigos das conexões [C - Cancelar]: ').upper()

        if connections != 'C':
            price = input('Insira o preço [C - Cancelar]: ')

            if price != 'C':
                try:
                    price = float(price)
                except Exception:
                    pass

                response = RoutesController.create(
                    connections=''.join(connections.split()).split('-'), price=price)

                if response['status_code'] == 201:
                    price = format_price(response["data"]["price"])

                    print('\nCadastro realizado')
                    print(f'{response["data"]["route"]}: R$ {price}\n')

                else:
                    print('\nNão foi possível cadastrar a rota desejada...')

                    if response.get('errors'):
                        print('Confira os dados inseridos.\n')

                    elif response['status_code'] == 500:
                        print('Erro interno - 500.\n')

        if input('Deseja cadastrar novamente [S/N]? ').upper() == 'S':
            RoutesView.create()

        return response if 'response' in locals() else None

    def read():
        clear_screen()

        print('\n======================\n'
              '        Rotas\n'
              '======================\n'
              '  Rotas devem filtradas no seguinte formato: \n\n'
              '   Origem: GRU\n'
              '  Destino: SCL\n'
              '======================\n')

        origin = input('Insira o código de origem [C - Cancelar]: ').upper()

        if origin != 'C':
            destiny = input('Insira o código de destino [C - Cancelar]: ').upper()

            if destiny != 'C':
                response = RouteController.read(
                    origin=origin, destiny=destiny)

                if response['status_code'] == 200:
                    price = format_price(response["data"]["price"])

                    print('\nMelhor preço')
                    print(f'{response["data"]["route"]}: R$ {price}\n')

                else:
                    print('\nNão foi possível encontrar a rota desejada...')

                    if response.get('errors'):
                        print('Confira os dados inseridos.\n')

                    elif response['status_code'] == 500:
                        print('Erro interno - 500.\n')

        if input('Deseja pesquisar novamente [S/N]? ').upper() == 'S':
            RoutesView.read()

        return response if 'response' in locals() else None
