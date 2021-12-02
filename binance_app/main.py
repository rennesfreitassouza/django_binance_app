from binance.spot import Spot as Client
from binance.error import ClientError
from django.conf import settings




def main(param={"value": None}):
    client = Client(base_url="https://testnet.binance.vision", key=settings.API_KEY, secret=settings.SECRET_KEY)

    try:
        if (param['value'] is None):
            param['value'] = 'BTCUSDT' #https://www.binance.com/pt-BR/trade/BTC_USDT
            
        response = client.avg_price(symbol=param['value'])
        
        retorno = {"Retorno": client.time(),
        "Current Average Price": response}
        print(retorno)
        return retorno
    except ClientError as error:
        str_error = "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message)
        print(str_error)

    return {'str_error': str_error}