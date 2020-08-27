from nepal_forex.conf import SUPPORTED_CURRENCIES
from nepal_forex.exceptions import CurrencyNotSupported


class Currency:
    """
    Country entity used in this package
    """

    def __init__(self, currency_code: str):
        self.currency_code = self._validate_currency_code(currency_code)

    @classmethod
    def _validate_currency_code(cls, value):
        if value in SUPPORTED_CURRENCIES:
            return value
        raise CurrencyNotSupported('Currency: {} not supported for now.'.format(value))

    def __str__(self):
        return self.currency_code
