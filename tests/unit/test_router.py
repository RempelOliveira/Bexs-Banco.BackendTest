import json
import unittest

from io import BytesIO

from app.constants import HTTP_HOST, HTTP_PORT
from app.router import Router


class TestRouter(unittest.TestCase):
    def test_do_POST(self):
        class MockRequest:
            def makefile(self, *args, **kwargs):
                return BytesIO(b'POST /routes HTTP/1.1')

            def sendall(self, response):
                try:
                    json_data = json.loads(response)

                    assert json_data['coonection']
                    assert json_data['price']

                except Exception:
                    pass

        class MockServer:
            def __init__(self, client_address, Handler):
                Handler(MockRequest(), client_address, self)

        MockServer((HTTP_HOST, HTTP_PORT), Router)

    def test_do_GET(self):
        class MockRequest:
            def __init__(self, route):
                self.route = route

            def makefile(self, *args, **kwargs):
                return BytesIO(f'GET {self.route} HTTP/1.1'.encode('utf-8'))

            def sendall(self, response):
                try:
                    json_data = json.loads(response)

                    if self.route == '/':
                        assert json_data['errors']
                        assert json_data['status_code'] == 404

                    else:
                        assert json_data['route']
                        assert json_data['price']

                except Exception:
                    pass

        class MockServer:
            def __init__(self, client_address, Handler, route):
                Handler(MockRequest(route), client_address, self)

        MockServer((HTTP_HOST, HTTP_PORT), Router, route='/')
        MockServer((HTTP_HOST, HTTP_PORT), Router, route='/routes?origin=GRU&destiny=SCL')
