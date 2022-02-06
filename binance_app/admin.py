from django.contrib import admin
from binance_app.models import TradingPair, TradingPairHash


# Register your models here.
admin.site.register(TradingPair)
admin.site.register(TradingPairHash)
