from binance.spot import Spot as Client
from binance.error import ClientError
from django.conf import settings
from binance_app.src.database import save_retorno


def main(param={'trading pair': None}):
    client = Client(key=settings.API_KEY, secret=settings.SECRET_KEY)
    retorno = dict(retorno={'str_error': '',
                            'symbol': {'trading pair symbol': '', 'price': 0},
                            'serverTime': 0})

    if (param['trading pair'] is None or param['trading pair'] != 'GXSUSDT'):
        param['trading pair'] = "BNBUSDT"
    retorno['retorno']['symbol']['trading pair symbol'] = param['trading pair']

    try:
        response = {}
        response = client.avg_price(symbol=param['trading pair'])

    except ClientError as error:
        str_error = "Error. status: {}, error code: {}, error message: {}"\
            .format(error.status_code, error.error_code, error.error_message)

        retorno['retorno']['str_error'] = str_error
    finally:
        retorno['retorno']['symbol']['price'] = response.get('price', 0)

    retorno['retorno']['serverTime'] = client.time().get('serverTime', 0)

    r = [retorno]
    save_retorno(r)
    return r
