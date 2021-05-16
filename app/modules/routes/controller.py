from app.modules.routes.model import RoutesModel

from app.decorators import validate, serialize
from app.modules.routes.serializer import RoutesSerializer, RouteSerializer

from app.errors.error_handler import ErrorHandler


class RoutesController:
    @validate(RoutesSerializer.input())
    @serialize(RoutesSerializer.output())
    def create(**kwargs):
        try:
            return {'data': RoutesModel.save(kwargs), 'status_code': 201}
        except Exception as e:
            return ErrorHandler.errors(e)


class RouteController:
    @validate(RouteSerializer.input())
    @serialize(RouteSerializer.output())
    def read(**kwargs):
        try:
            return {'data': RoutesModel.find_one(kwargs), 'status_code': 200}
        except Exception as e:
            return ErrorHandler.errors(e)
