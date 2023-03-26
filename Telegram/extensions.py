import requests
import json
from config import keys

class APIException(Exception):
    pass

class Convert:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException('Введите разные вылюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалость обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалость обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалость обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base