# Django Binance App

## Prerequisites

- [Your own Binance API](https://www.binance.com/en/support/faq/360002502072)
- Modules 'Django' 'django-allauth', 'django-environ', 'django-filter', 'django-rest-framework', 'binance-connector'

## How to run the django app

- Install Python 3
- Create a virtual environment
- Install the required modules
- Execute these commands:<p>
  `$ python manage.py migrate`<p>
  `$ python manage.py createsuperuser`<p>
  `$ python manage.py runserver`<p>
  `Execute a HTTP GET request:`<p>

          GET /binance_app/exec_request HTTP/1.1
          Host: 127.0.0.1:8000
          Authorization: Basic 'base64encodedstr(username:password)'
          Content-Type: application/json
          Content-Length: 35

          {
              "trading pair": "GXSUSDT"
          }

## About the Binance public API endpoint

[Current Average Price](https://binance-connector.readthedocs.io/en/stable/binance.spot.market.html#current-average-price)

## Future development

Django + [JavaScript](https://docs.djangoproject.com/en/3.2/internals/contributing/writing-code/javascript/)

`from decimal import *; a = Decimal('.10'); b = Decimal('.39'); c = Decimal('.09'); x = a + a + a + c - b`

## About this solution

[Mozzato](https://mozzatto.com.br/) challenge <p>[About binance Python module](https://github.com/binance/binance-connector-python)
