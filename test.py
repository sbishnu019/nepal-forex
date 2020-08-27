from nepal_forex import nepal_forex

print(nepal_forex.exchange_rate(currency='USD', date='2020-08-27'))

print(nepal_forex.convert_from(amount=100, currency='USD', decimal_places=4))
print(nepal_forex.convert_to(amount=160, currency='USD', decimal_places=4))
