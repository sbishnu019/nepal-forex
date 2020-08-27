# Nepal ForEx

Nepal ForEx is a Python package for making Currency Exchange easier and fast between NPR and Foreign Currencies.

It parses current exchange rate from Nepal Rastra Bank.
Exchange rates are genuine and realtime provided by Nepal Rastra Bank.

#### Supported Currencies
* INR
* USD
* EUR
* GBP
* CHF
* AUD
* CAD
* SGD
* JPY
* CNY
* SAR
* QAR
* THB
* AED
* MYR
* KRW
* SEK
* DKK
* HKD
* BHD



## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nepal-forex.

```bash
pip install nepal-forex
```

## Usage
Nepal ForEx

To get NPR exchange rate of specified currency on specified date.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.exchange_rate(currency='USD', date='2020-08-27')      # Decimal('118.58')
```

To get NPR exchange rate of specified currency of today.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.exchange_rate(currency='USD')                        # Decimal('118.58')
```

To convert NPR amount to specified currency of today exchange rate.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.convert_to(amount=160, currency='USD')               # Decimal('1.35')
```

To convert NPR amount to specified currency of specified date exchange rate.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.convert_to(amount=160, currency='USD', date='2020-08-27')            # Decimal('1.35')
```

To convert specified currency amount to NPR of today exchange rate.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.convert_from(amount=100, currency='USD')             # Decimal('11858.00')
```

To convert specified currency amount to NPR of specified date exchange rate.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.convert_from(amount=100, currency='USD', date='2020-08-27')      # Decimal('11858.00')
```

Also Decimal places can be set.
```python
from nepal_forex.nepal_forex import nepal_forex

nepal_forex.convert_to(amount=160, currency='USD', date='2020-08-27', decimal_places=4)      # Decimal('1.3582')
```





## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)