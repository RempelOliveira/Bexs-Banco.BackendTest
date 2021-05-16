import json

from urllib.parse import urlparse, parse_qsl
from http.server import SimpleHTTPRequestHandler

from app.modules.routes.controller import RoutesController, RouteController


class Router(SimpleHTTPRequestHandler):
    routes = {
        'GET': {'/routes': RouteController}, 'POST': {'/routes': RoutesController}
    }

    def do_POST(self):
        json_data = json.loads(
            self.rfile.read(int(self.headers.get('content-length', 0))) or '{}')

        controller = self._init_controller()

        if controller:
            controller_response = controller.create(
                **json_data)

            self._response(controller_response)

    def do_GET(self):
        controller = self._init_controller()

        if controller:
            controller_response = controller.read(
                **dict(parse_qsl(self.parsed_url.query)))

            self._response(controller_response)

    def _init_controller(self):
        self.parsed_url = urlparse(self.path)

        for route in self.routes.get(self.command).keys():
            if self.parsed_url.path == route:
                return self.routes[self.command][route]

        self._response({'errors': {'resource': 'not found'}, 'status_code': 404})

    def _response(self, response):
        self.send_response(response['status_code'])

        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = response.get('data') or \
            response.get('errors')

        if json_response:
            self.wfile.write(bytes(json.dumps(json_response), 'utf-8'))
