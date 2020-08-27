from nepal_forex.datasets import CURRENCY_DATA

NRB_API = 'https://archive.nrb.org.np/exportForexJSON.php'

SUPPORTED_CURRENCIES = [
    key for key in CURRENCY_DATA.keys()
]
