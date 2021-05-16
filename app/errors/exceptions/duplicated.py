class Duplicated(Exception):
    def __init__(self):
        self.errors = {'connections': 'duplicated data'}
        self.status_code = 422
