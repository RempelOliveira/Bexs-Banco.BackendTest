import unittest
from app.utils import clear_screen, format_price, has_duplicates


class TestUtils(unittest.TestCase):
    def test_clear_screen(self):
        assert not clear_screen()

    def test_format_price(self):
        assert format_price(10)
        assert format_price(10.0)
        assert format_price(10.00)

        with self.assertRaises(TypeError):
            assert not format_price()

        with self.assertRaises(ValueError):
            assert not format_price('')
            assert not format_price('10')

    def test_has_duplicates(self):
        assert has_duplicates(['GRU', 'GRU'])
        assert not has_duplicates(['GRU', 'SCL'])
