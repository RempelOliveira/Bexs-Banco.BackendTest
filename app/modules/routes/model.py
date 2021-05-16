import csv
import operator

from pathlib import Path

from app.utils import has_duplicates
from app.constants import DATA_PATH, DATA_FILE

from app.errors.error_handler import Duplicated, RecordNotFound


class RoutesModel:
    def save(data):
        if has_duplicates(data['connections']):
            raise Duplicated

        Path(DATA_PATH).mkdir(exist_ok=True)

        with open(f'{DATA_PATH}/{DATA_FILE}', 'a+') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(data['connections'] + [data['price']])

        return {
            'route': ' -> '.join(data['connections']),
            'price': data['price']
        }

    def find_one(data):
        if has_duplicates([data['origin'], data['destiny']]):
            raise Duplicated

        prices = {}

        if Path(f'{DATA_PATH}/{DATA_FILE}').is_file():
            with open(f'{DATA_PATH}/{DATA_FILE}', 'r') as file:
                routes = file.read().splitlines()

                for i, route in enumerate(routes):
                    connections = route.split(',')

                    try:
                        if connections.index(data['origin']) < connections.index(data['destiny']):
                            prices[i] = connections[-1]

                    except Exception:
                        continue

        if not prices:
            raise RecordNotFound

        price = min(prices.items(), key=operator.itemgetter(1))

        return {
            'route': ' -> '.join((routes[price[0]].split(',')[0:-1])),
            'price': float(price[1])
        }
