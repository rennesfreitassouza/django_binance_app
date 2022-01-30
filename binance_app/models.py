from django.db import models


# GXS to USDT market on Binance exchange
class GXStoUSDT(models.Model):
    gxsusdt_avg_price = models.FloatField()
    gxsusdt_dt = models.DateTimeField()
