import unittest

from app.modules.routes.serializer import RouteSerializer, RoutesSerializer


class TestRouteSerializer(unittest.TestCase):
    def test_input(self):
        serializer = RouteSerializer.input()

        for field in serializer:
            assert type(serializer[field]) == dict

    def test_output(self):
        serializer = RouteSerializer.output()

        for field in serializer:
            assert type(serializer[field]) == type


class TestRoutesSerializer(unittest.TestCase):
    def test_input(self):
        serializer = RoutesSerializer.input()

        for field in serializer:
            assert type(serializer[field]) == dict

    def test_output(self):
        serializer = RoutesSerializer.output()

        for field in serializer:
            assert type(serializer[field]) == type
