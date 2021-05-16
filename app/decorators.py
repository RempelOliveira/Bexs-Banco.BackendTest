from functools import wraps
from app.serializer_validator import SerializerValidator


def validate(schema):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            validator = SerializerValidator(schema)
            validator.data = kwargs

            if not validator.validate():
                return {'errors': validator.errors, 'status_code': 422}

            return func(*args, **validator.normalized_data())

        return wrapper
    return inner_function


def serialize(schema):
    def inner_function(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)

            if response.get('data'):
                serializer = SerializerValidator(schema)
                serializer.data = response['data']

                response.update({'data': serializer.serialized_data()})

            else:
                response.update({'data': None})

            return response

        return wrapper
    return inner_function
