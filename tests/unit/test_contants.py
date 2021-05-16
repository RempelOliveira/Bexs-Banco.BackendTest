import unittest

from app.constants import HTTP_HOST, HTTP_PORT, DATA_PATH, DATA_FILE


class TestConstants(unittest.TestCase):
    def test_http_post(self):
        assert type(HTTP_HOST) == str

    def test_http_port(self):
        assert type(HTTP_PORT) == int

    def test_data_path(self):
        assert type(DATA_PATH) == str

    def test_data_file(self):
        assert type(DATA_FILE) == str
