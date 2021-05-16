import sys

from http.server import HTTPServer

from app.router import Router
from app.constants import HTTP_HOST, HTTP_PORT

from app.modules.menu.view import MenuView


if __name__ == '__main__':
    if '--console' not in sys.argv:
        server = HTTPServer((HTTP_HOST, HTTP_PORT), Router)

        print(f'* Running on http://{HTTP_HOST}:{HTTP_PORT}')
        print('* Press CTRL+C to quit')

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.socket.close()

    else:
        MenuView.show()
