class SerializerValidator:
    def __init__(self, schema):
        self.data = None
        self.errors = {}

        self.schema = schema

    def validate(self):
        for field, rules in self.schema.items():
            value = self.data.get(field)

            if rules['required'] and not value:
                self.errors.update({field: 'required'})

            else:
                if rules['type'] == str:
                    if type(value) == float or str(value).isnumeric():
                        self.errors.update({field: 'invalid data type'})

                        continue

                    self.data[field] = value.strip()

                if type(value) != rules['type']:
                    self.errors.update({field: 'invalid data type'})

                elif rules['type'] == list:
                    if len(value) < rules['items']['minitems']:
                        self.errors.update({field: 'invalid amount of items'})
                    else:
                        for k, v in enumerate(value):
                            if not v:
                                self.errors.update({field: {'items': 'required'}})

                            elif type(v) != rules['items']['type']:
                                self.errors.update({field: {'items': 'invalid data type'}})

                            elif rules['items']['type'] == str:
                                if type(v) == float or str(v).isnumeric():
                                    self.errors.update({field: {'items': 'invalid data type'}})

                                else:
                                    self.data[field][k] = v.strip()

        return True if not self.errors else False

    def normalized_data(self):
        for field in [x for x in self.data if x not in self.schema]:
            self.data.pop(field)

        return self.data

    def serialized_data(self):
        data = self.normalized_data()

        for field, value in data.items():
            if not value:
                data.update({field: None})

            else:
                data_type = self.schema.get(field)

                if data_type and not type(value) == data_type:
                    data.update({field: data_type(value)})

        return data
