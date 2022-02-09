from django.utils.timezone import make_aware
from django.conf import settings
from pytz import timezone
from binance_app.models import TradingPair, TradingPairHash
from django.db.utils import IntegrityError
from datetime import datetime
import base64
import hashlib


def save_retorno(result):
    d_result = result[0]['retorno']

    trading_pair_symbol = d_result['symbol']['trading pair symbol']
    symbol_avg_price = d_result['symbol']['price']

    aware_datetime = convert_to_datetime(d_result['serverTime'])

    api_dt = aware_datetime

    error = d_result['str_error']

    tp_row = TradingPair(trading_pair_symbol=trading_pair_symbol,
                         symbol_avg_price=symbol_avg_price,
                         api_dt=api_dt,
                         error=error)
    tp_row.save()

    save_trading_pair_hash(tp_row)


def save_trading_pair_hash(tp_row):
    tp_row_hash = hash_data(str(tp_row))
    tp_hash_row = TradingPairHash(trading_pair=tp_row, hash=tp_row_hash)

    try:
        tp_hash_row.save()
    except IntegrityError as e:
        tp_row.update(
            error=f'{tp_row.error};  new_error: {e} hash: {tp_row_hash}')


def convert_to_datetime(server_timestamp):
    timezone_local = timezone(settings.TIME_ZONE)
    aware_datetime = make_aware(value=datetime.fromtimestamp(
        server_timestamp / 1000),
        timezone=timezone_local)
    return aware_datetime


def hash_data(m1: str):
    m1_encoded = m1.encode('utf-8')
    m1_encoded_hex = hashlib.md5(m1_encoded).hexdigest()
    m1_encoded_hex_b64 = base_64(m1_encoded_hex)
    return m1_encoded_hex_b64


def base_64(message: str):
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)

    base64_message = base64_bytes.decode('utf-8')

    return base64_message
