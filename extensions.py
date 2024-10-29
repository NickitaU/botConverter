import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def APIException(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException("Валюта 1 и та же")

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise ConvertionException(f'Ну удалось обработать валюту {quote}')

        try:
            base_ticket = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException("Не удалось обработать количество валюты")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        t_base = json.loads(r.content)[keys[base]]

        return t_base * amount
