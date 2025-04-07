currencies = ['USD', 'EUR', 'JPY', 'GBP']
conversion_rates = [1, 1.08, 0.00663, 1.3]

def convert_currency(base_currency, base_value, currency_to_convert):

    usd_conversion = base_value / conversion_rates[currencies.index(base_currency)]
    
    final_conversion = usd_conversion * conversion_rates[currencies.index(currency_to_convert)]

    return round(final_conversion, 2)

def currency_conversion_menu():

    while True:

        base_currency = ''

        while True: 
            match input('Select a base currency: \n1. United States Dollar \n2. Euro \n3. Pound \n4. Yen \n5. Exit \n'):

                # United States Dollar
                case '1':
                    base_currency = 'USD'
                    break

                # Euro
                case '2':
                    base_currency = 'EUR'
                    break

                # Pound
                case '3':
                    base_currency = 'GBP'
                    break
                
                case '4':
                    base_currency = 'JPY'
                    break
                
                case '5':
                    print('Exitting...')
                    break

        base_value = 0

        while True:
            try:
                base_value = float(input('Amount of currency to convert: '))
            except:
                print('Invalid Input')
                continue

            if base_value <= 0:
                print('Invalid Input')
                continue
            else:
                break

        currency_to_convert = ''

        while True:
            match input('Select a currency to convert to: \n1. United States Dollar \n2. Euro \n3. Pound \n4. Yen \n5. Exit \n'):

                # United States Dollar
                case '1':
                    currency_to_convert = 'USD'
                    break

                # Euro
                case '2':
                    currency_to_convert = 'EUR'
                    break

                # Pound
                case '3':
                    currency_to_convert = 'GBP'
                    break
                
                case '4':
                    currency_to_convert = 'JPY'
                    break
                
                case '5':
                    print('Exitting...')
                    break

        return convert_currency(base_currency, base_value, currency_to_convert)

# print(currency_conversion_menu())


