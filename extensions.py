import requests
import json
from config import currency


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount):

        try:
            from_currency = currency[quote.lower()]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {quote}')

        try:
            to_currency = currency[base.lower()]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}')

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {amount}')

        query = from_currency + '_' + to_currency
        r = requests.get(f'https://free.currconv.com/api/v7/convert?apiKey=cd2ff852330c08894153&q={query}&compact=ultra')
        total_base = json.loads(r.content)[query] * amount
        total_base = round(total_base, 3)

        return total_base
