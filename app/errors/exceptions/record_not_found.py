class RecordNotFound(Exception):
    def __init__(self):
        self.errors = {'route': 'not found'}
        self.status_code = 404
