from django import forms


class BinanceAppFormChoice(forms.Form):
    trading_pair_symbol = forms.ChoiceField(label="Trading pair symbol",
                                            choices=[(None, ''),
                                                     ('GXSUSDT', 'GXSUSDT'),
                                                     ('BNBUSDT', 'BNBUSDT')])
