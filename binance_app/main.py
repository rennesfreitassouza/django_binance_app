from binance.spot import Spot as Client
from binance.error import ClientError


def main(param={"value": None}):
    client = Client(base_url='https://testnet.binance.vision')

    try:
        
        return {"Retorno": client.time()}
    except ClientError as error:
        str_error = "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message)
        print(str_error)

    return {'str_error': str_error}
