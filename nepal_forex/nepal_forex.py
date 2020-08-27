from datetime import datetime
from decimal import Decimal, getcontext, ROUND_HALF_UP

import requests

from nepal_forex.conf import NRB_API
from nepal_forex.entities import Currency
from nepal_forex.exceptions import (
    InvalidDateFormat,
    FetchDataFailed,
    ProviderResponseConflict,
    CurrencyNotFound
)


class NRBCurrencyModel:
    """
    Data model for data fetched from NRB
    """
    def __init__(self, **kwargs):
        self.date = kwargs.get('date')
        self.base_currency = kwargs.get('base_currency')
        self.target_currency = kwargs.get('target_currency')
        self.base_value = kwargs.get('base_value')
        self.target_buy = kwargs.get('target_buy')
        self.target_sell = kwargs.get('target_sell')

    def __str__(self):
        return self.base_currency

    def __repr__(self):
        return self.base_currency


class NepalForEx:
    """
     Class for Nepal ForeEx

    """
    date_str_format = '%Y-%m-%d'

    def exchange_rate(self, currency: str, date=None):
        """
        Use this to get exchange rate of NPR to specific currency

        :param currency: Currency you need the exchange rate.
        :type currency: str
        :param date: date of exchange rate, if null default is today.
        :type date: %Y-%m-%d
        :return: exchange rate
        :rtype: Decimal
        """
        currency = Currency(currency)
        date = self._get_date(date)
        data = self._load_data(date=date)

        requested_currency = self._search_on_data(
            data=data,
            currency=currency.currency_code
        )
        return Decimal(requested_currency.target_buy)

    def _load_data(self, date: datetime):
        data = []
        param = {
            'YY': date.year,
            'MM': '{:02d}'.format(date.month),
            'DD': '{:02d}'.format(date.day),
        }

        response = requests.get(
            url=NRB_API,
            params=param
        )
        response_json = response.json()
        if response.status_code != 200:
            raise FetchDataFailed('Fetching data from NRB failed.')

        try:
            for currency in response_json.get('Conversion').get('Currency'):
                kwargs = {
                    'date': currency.get('Date'),
                    'base_currency': currency.get('BaseCurrency'),
                    'target_currency': currency.get('TargetCurrency'),
                    'base_value': Decimal(currency.get('BaseValue')),
                    'target_buy': Decimal(currency.get('TargetBuy')) if currency.get('TargetBuy') else None,
                    'target_sell': Decimal(currency.get('TargetSell')),
                }
                data.append(
                    NRBCurrencyModel(**kwargs)
                )
        except TypeError:
            raise ProviderResponseConflict('Provider response conflict - contact administrator.')

        return data

    def _search_on_data(self, data: list, currency: str):
        for i in range(len(data)):
            if data[i].base_currency == currency:
                return data[i]
        raise CurrencyNotFound('Currency not found - contact administrator.')

    def convert_to(self, currency: str, amount: Decimal, decimal_places=2, date=None):
        """
        Use this to convert NPR amount to specified currency

        :param amount: amount to be converted
        :type amount: str
        :param currency: currency to be in converted
        :type currency: str
        :param decimal_places: decimal places in resulting amount
        :type decimal_places: int
        :param date: to apply certain date exchange rate, on default its for today
        :return: converted amount
        :rtype: Decimal
        """
        currency = Currency(currency)

        date = self._get_date(date)

        data = self._load_data(date=date)

        convert_to_currency = self._search_on_data(
            data=data,
            currency=currency.currency_code
        )

        if convert_to_currency.base_currency == 'INR':
            result_value = Decimal(
                Decimal(amount) * (convert_to_currency.base_value/convert_to_currency.target_buy)
            )
        else:
            result_value = Decimal(
                Decimal(amount) * (convert_to_currency.base_value / convert_to_currency.target_buy),
            )
        return Decimal(result_value.quantize(
            Decimal(10) ** -decimal_places,
            rounding=ROUND_HALF_UP
        ))

    def convert_from(self, currency: str, amount: Decimal, decimal_places=2, date=None):
        """
        Use this to convert to NPR from specified currency

        :param amount: amount to be converted
        :type amount: str
        :param currency: currency to be in converted
        :type currency: str
        :param decimal_places: decimal places in resulting amount
        :type decimal_places: int
        :param date: to apply certain date exchange rate, on default its for today
        :return: converted amount
        :rtype: Decimal
        """

        currency = Currency(currency)

        date = self._get_date(date)

        data = self._load_data(date=date)

        convert_from_currency = self._search_on_data(
            data=data,
            currency=currency.currency_code
        )

        if convert_from_currency.base_currency == 'INR':
            result_value = Decimal(Decimal(amount) * (convert_from_currency.target_buy/convert_from_currency.base_value))
        else:
            result_value = Decimal(
                Decimal(amount) * convert_from_currency.target_buy
            )
        return Decimal(result_value.quantize(
            Decimal(10) ** -decimal_places,
            rounding=ROUND_HALF_UP
        ))

    def _get_date(self, date=None):
        if date:
            try:
                return datetime.strptime(date, self.date_str_format)
            except ValueError:
                raise InvalidDateFormat(
                    'date: {} does not match format: {}'.format(
                        date,
                        self.date_str_format
                    )
                )
        else:
            return datetime.now()


nepal_forex = NepalForEx()
