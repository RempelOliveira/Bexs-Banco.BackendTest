import unittest

from app.serializer_validator import SerializerValidator
from app.modules.routes.serializer import RoutesSerializer, RouteSerializer


class TestSerializerValidator(unittest.TestCase):
    def test_validate(self):
        validator = SerializerValidator(RoutesSerializer.input())
        validator.data = {
            'connections': ['GRU', 'SCL'],
            'price': 120.0
        }

        assert validator.validate()

        validator.data = {
            'connections': None,
            'price': None
        }

        assert not validator.validate()

        validator.data = {
            'connections': '10',
            'price': '10'
        }

        assert not validator.validate()

        validator.data = {
            'connections': [''],
            'price': 120
        }

        assert not validator.validate()

        validator.data = {
            'connections': [120],
            'price': 120
        }

        assert not validator.validate()

        validator.data = {
            'connections': ['', 120],
            'price': 120
        }

        assert not validator.validate()

        validator.data = {
            'connections': ['120', 'GRU'],
            'price': 120
        }

        assert not validator.validate()

        validator = SerializerValidator(RouteSerializer.input())
        validator.data = {
            'origin': '120',
            'destiny': '120'
        }

        assert not validator.validate()

    def test_normalized_data(self):
        validator = SerializerValidator(RoutesSerializer.input())
        validator.data = {
            'connections': ['GRU', 'SCL'],
            'price': 120.0
        }

        assert validator.normalized_data() == validator.data

        validator.data = {
            'field': ''
        }

        assert validator.normalized_data() == validator.data

    def test_serialized_data(self):
        validator = SerializerValidator(RoutesSerializer.output())
        validator.data = {
            'connections': ['GRU', 'SCL'],
            'price': 0
        }

        assert validator.serialized_data() == validator.data

        validator.data = {
            'connections': ['GRU', 'SCL'],
            'price': 120
        }

        assert validator.serialized_data() == validator.data

        validator.data = {
            'connections': ['GRU', 'SCL'],
            'price': '120.0'
        }

        assert validator.serialized_data() == validator.data
