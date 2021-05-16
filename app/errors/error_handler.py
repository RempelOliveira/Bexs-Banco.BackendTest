import ast

from app.errors.exceptions.duplicated import Duplicated
from app.errors.exceptions.record_not_found import RecordNotFound


class ErrorHandler:
    def errors(e):
        response = {
            'status_code': getattr(e, 'status_code', 500)
        }

        if type(e) in [Duplicated, RecordNotFound]:
            response.update({'errors': ast.literal_eval(str(e.errors))})

        return response
