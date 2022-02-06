from django.db import models


# Trading Pair data from Binance API
class TradingPair(models.Model):
    trading_pair_symbol = models.CharField(max_length=10)
    symbol_avg_price = models.FloatField()
    api_dt = models.DateTimeField()
    error = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'< id: {self.id} trading_pair_symbol:\
            {self.trading_pair_symbol} symbol_avg_price: {self.symbol_avg_price}\
            api_dt: {self.api_dt} error: {self.error} >'


class TradingPairHash(models.Model):
    trading_pair = models.OneToOneField(
        TradingPair, on_delete=models.CASCADE, parent_link=True, primary_key=True)

    hash = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return f'{self.hash}'
