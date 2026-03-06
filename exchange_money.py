def exchange_money(budget, exchange_rate):
    foreign_currency = budget / exchange_rate
    return foreign_currency

resultado = exchange_money(200, 0.0075)
print(resultado)
