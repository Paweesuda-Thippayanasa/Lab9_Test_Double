# นางสาวปวีณ์สุดา ทิพยนาสา 653380137-5
import requests
from datetime import datetime
from unittest.mock import Mock


class CurrencyExchanger:
    def __init__(self, base_currency="THB", target_currency="USD"):
        self.currency_api = "https://coc-kku-bank.com/foreign-exchange"
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.ex_date = datetime.today().date()
        self.api_response = None

    def get_currency_rate(self):
        try:
            # get the exchange rate
            p = {'from': self.base_currency, 'to': self.target_currency}
            response = requests.get(self.currency_api, params=p)
            if response.status_code in (200, 201):
                self.api_response = response.json()
        except requests.exceptions.RequestException:
            self.api_response = None


    # def currency_exchange(self, amount):
    #     self.get_currency_rate()
    #     # Implement function to calculate the currency from base currency to the target currency
    #     return amount

    def currency_exchange(self, amount):
        self.get_currency_rate()
        if self.api_response and 'result' in self.api_response and self.target_currency in self.api_response['result']:
            rate = self.api_response['result'][self.target_currency]
            return amount * rate
        return 0  # Return 0 or handle the case where the rate is not available
