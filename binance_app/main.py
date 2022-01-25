from binance.spot import Spot as Client
from binance.error import ClientError
from django.conf import settings


def main(param={"trading pair": None}):
    client = Client(key=settings.API_KEY, secret=settings.SECRET_KEY)

    try:
        if (param['trading pair'] is None):
            param['trading pair'] = 'BNBUSDT'

        response = client.avg_price(symbol=param['trading pair'])

        retorno = {"Retorno": client.time(),
                   f"{param['trading pair']} current average price": response}

        return retorno
    except ClientError as error:
        str_error = "Found error. status: {}, error code: {},\
            error message: {}".format(
            error.status_code, error.error_code, error.error_message)
        print(str_error)

    return {'str_error': str_error}
