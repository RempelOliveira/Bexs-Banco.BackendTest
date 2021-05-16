import os
import unittest
import requests
import threading

from unittest.mock import patch
from http.server import HTTPServer

from app.router import Router
from app.constants import HTTP_HOST, HTTP_PORT, DATA_PATH


class TestRoutes(unittest.TestCase):
    api_address = f'http://{HTTP_HOST}:{HTTP_PORT}'

    @classmethod
    def setUpClass(self):
        server = HTTPServer((HTTP_HOST, HTTP_PORT), Router)

        self.server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        self.server_thread.start()

    @classmethod
    def tearDownClass(self):
        os.remove(f'{DATA_PATH}/routes_test.csv')
        self.server_thread._is_stopped = True

    @patch('app.modules.routes.model.DATA_FILE', 'routes_test.csv')
    def test_create(self):
        response = requests.post(
            f'{self.api_address}/routes', json={}
        )

        assert response.status_code == 422

        response = requests.post(
            f'{self.api_address}/routes', json={'connections': ['GRU', 'SCL'], 'price': 120.0}
        )

        assert response.status_code == 201

        response = requests.post(
            f'{self.api_address}/routes', json={'connections': ['GRU', 'GRU'], 'price': 120.0}
        )

        assert response.status_code == 422

        with patch('app.modules.routes.model.DATA_FILE', ''):
            response = requests.post(
                f'{self.api_address}/routes', json={'connections': ['GRU', 'SCL'], 'price': 120.0}
            )

        assert response.status_code == 500

    @patch('app.modules.routes.model.DATA_FILE', 'routes_test.csv')
    def test_read(self):
        response = requests.get(
            f'{self.api_address}/routes', params={}
        )

        assert response.status_code == 422

        response = requests.get(
            f'{self.api_address}/routes', params={'origin': 'GRU', 'destiny': 'GRU'}
        )

        assert response.status_code == 422

        response = requests.get(
            f'{self.api_address}/routes', params={'origin': 'RGU', 'destiny': 'LCS'}
        )

        assert response.status_code == 404

        response = requests.get(
            f'{self.api_address}/routes', params={'origin': 'GRU', 'destiny': 'SCL'}
        )

        assert response.status_code == 200
