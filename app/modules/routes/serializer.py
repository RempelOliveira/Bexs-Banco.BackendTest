class RoutesSerializer:
    def input():
        return {
            'connections': {
                'type': list,
                'required': True,
                'items': {
                    'type': str,
                    'minitems': 2
                }
            },
            'price': {
                'type': float,
                'required': True
            }
        }

    def output():
        return {
            'route': str,
            'price': float
        }


class RouteSerializer:
    def input():
        return {
            'origin': {
                'type': str,
                'required': True
            },
            'destiny': {
                'type': str,
                'required': True
            }
        }

    def output():
        return {
            'route': str,
            'price': float
        }
