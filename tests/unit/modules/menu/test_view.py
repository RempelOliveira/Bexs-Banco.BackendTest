import os
import unittest

from unittest.mock import patch

from app.constants import DATA_PATH
from app.modules.menu.view import MenuView


class TestRoutes(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        os.remove(f'{DATA_PATH}/routes_test.csv')

    @patch('app.modules.routes.model.DATA_FILE', 'routes_test.csv')
    def test_show(self):
        with patch('builtins.input', side_effect=['1', 'GRU - SCL', '120', 'N', '3']):
            assert not MenuView.show()

        with patch('builtins.input', side_effect=['2', 'GRU', 'SCL', 'N', '3']):
            assert not MenuView.show()

        with patch('builtins.input', side_effect=['5', '3', '3']):
            assert not MenuView.show()
