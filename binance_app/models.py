from django.db import models


# GXS to USDT market on Binance exchange
class GXStoUSDT(models.Model):
    trading_pair_symbol = models.CharField(max_length=10)
    symbol_avg_price = models.FloatField()
    api_dt = models.DateTimeField()
    error = models.CharField(max_length=255)
