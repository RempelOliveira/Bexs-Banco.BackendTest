import os
import unittest

from unittest.mock import patch

from app.constants import DATA_PATH
from app.modules.routes.view import RoutesView


class TestRoutes(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        os.remove(f'{DATA_PATH}/routes_test.csv')

    @patch('app.modules.routes.model.DATA_FILE', 'routes_test.csv')
    def test_create(self):
        with patch('builtins.input', side_effect=['GRU - SCL', '120', 'N']):
            response = RoutesView.create()

            assert response['data']
            assert response['status_code'] == 201

        with patch('builtins.input', side_effect=[
                'GRU - SCL', '120', 'S', 'GRU - SCL', '120', 'N']):
            response = RoutesView.create()

            assert response['data']
            assert response['status_code'] == 201

        with patch('builtins.input', side_effect=['', '120', 'N']):
            response = RoutesView.create()

            assert response['errors']
            assert response['status_code'] == 422

        with patch('builtins.input', side_effect=['', 'GRU', 'N']):
            response = RoutesView.create()

            assert response['errors']
            assert response['status_code'] == 422

        with patch('app.modules.routes.model.DATA_FILE', ''):
            with patch('builtins.input', side_effect=['GRU - SCL', '120', 'N']):
                response = RoutesView.create()

                assert not response['data']
                assert response['status_code'] == 500

    @patch('app.modules.routes.model.DATA_FILE', 'routes_test.csv')
    def test_read(self):
        with patch('builtins.input', side_effect=['GRU', 'SCL', 'N']):
            response = RoutesView.read()

            assert response['data']
            assert response['status_code'] == 200

        with patch('builtins.input', side_effect=['RGU', 'LCS', 'N']):
            response = RoutesView.read()

            assert not response['data']
            assert response['status_code'] == 404

        with patch('builtins.input', side_effect=['RGU', '', 'N']):
            response = RoutesView.read()

            assert response['errors']
            assert response['status_code'] == 422

        with patch('builtins.input', side_effect=['GRU', 'SCL', 'S', 'GRU', 'SCL', 'N']):
            response = RoutesView.read()

            assert response['data']
            assert response['status_code'] == 200

        with patch('app.modules.routes.model.RoutesModel.find_one', side_effect=Exception):
            with patch('builtins.input', side_effect=['GRU', 'SCL', 'N']):
                response = RoutesView.read()

                assert not response['data']
                assert response['status_code'] == 500
