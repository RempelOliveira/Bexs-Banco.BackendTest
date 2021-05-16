import unittest

from app.errors.error_handler import ErrorHandler

from app.errors.exceptions.duplicated import Duplicated
from app.errors.exceptions.record_not_found import RecordNotFound


class TestErrorHandler(unittest.TestCase):
    def test_errors(self):
        try:
            raise ValueError
        except Exception as e:
            assert ErrorHandler.errors(e) == {'status_code': 500}

        try:
            raise Duplicated
        except Exception as e:
            assert ErrorHandler.errors(e) == \
                {'status_code': 422, 'errors': {'connections': 'duplicated data'}}

        try:
            raise RecordNotFound
        except Exception as e:
            assert ErrorHandler.errors(e) == \
                {'status_code': 404, 'errors': {'route': 'not found'}}
