from django.utils.timezone import make_aware
from django.conf import settings

from pytz import timezone

from binance_app.models import GXStoUSDT
from datetime import datetime


def save_retorno(result):
    d_result = result[0]['retorno']

    trading_pair_symbol = d_result['symbol']['trading pair symbol']
    symbol_avg_price = d_result['symbol']['price']

    aware_datetime = convert_to_datetime(d_result['serverTime'])

    api_dt = aware_datetime
    error = d_result['str_error']

    GXStoUSDT.objects.create(trading_pair_symbol=trading_pair_symbol,
                             symbol_avg_price=symbol_avg_price,
                             api_dt=api_dt, error=error)


def convert_to_datetime(server_timestamp):
    timezone_local = timezone(settings.TIME_ZONE)
    aware_datetime = make_aware(value=datetime.fromtimestamp(
        server_timestamp / 1000),
        timezone=timezone_local)
    return aware_datetime
