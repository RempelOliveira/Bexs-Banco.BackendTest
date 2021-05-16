import unittest

from app.decorators import validate, serialize
from app.modules.routes.serializer import RoutesSerializer


class TestDecorators(unittest.TestCase):
    def test_validate(self):
        @validate(RoutesSerializer.input())
        def valid(**kwargs):
            return True

        assert valid(connections='GRU - SCL', price=120.0)

        @validate(RoutesSerializer.input())
        def invalid(**kwargs):
            return

        response = invalid(connections='GRU - SCL', price='')

        assert response['errors']
        assert response['status_code'] == 422

    def test_serialize(self):
        @serialize(RoutesSerializer.output())
        def with_data(**kwargs):
            return {'data': {'route': 'GRU -> SCL', 'price': 120}, 'status_code': 201}

        response = with_data(connections='GRU - SCL', price=120)

        assert response['data']
        assert response['status_code'] == 201

        @serialize(RoutesSerializer.output())
        def without_data(**kwargs):
            return {}

        response = without_data(connections=None, price=120)

        assert not response['data']
