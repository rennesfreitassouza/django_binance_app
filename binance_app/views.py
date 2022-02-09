from binance_app import main
from rest_framework.response import Response
from rest_framework.decorators import api_view
from binance_app.src.log import Log
from datetime import datetime
from django.shortcuts import render, redirect
from binance_app.models import TradingPair
from binance_app.forms import BinanceAppFormChoice
from django.http import JsonResponse


@api_view(('GET',))
def exe(request):
    if request.method == 'GET':

        logging_v_ip(request)

        body = request.data

        data = main.main(param={"trading pair": body['trading pair']})

        return Response(data)
    return


def execute_new_req(request):
    if request.method == 'GET':
        logging_v_ip(request)
        filled_form = BinanceAppFormChoice(request.GET)
        if filled_form.is_valid():
            body = {
                'trading pair': filled_form.cleaned_data["trading_pair_symbol"]}

            main.main(param={"trading pair": body['trading pair']})
        return redirect('home')
    return JsonResponse({'test': 'test'})


def logging_v_ip(request):
    log = Log("exe view")

    log.set_warning_msg(
        "\U0001F600 - view CALLED AT %s" % datetime.now()
        .strftime("%Y-%m-%d %I:%M:%S %z"))

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        v_ip = x_forwarded_for.split(',')[0]
    else:
        v_ip = request.META.get('REMOTE_ADDR')

    log.set_warning_msg("\U0001F600 - view called by %s"
                        % str(v_ip))


def home(request):

    binanceappformchoice = BinanceAppFormChoice()

    trading_pair = TradingPair.objects.all().order_by('-api_dt')[:5]

    return render(request, 't_b_app/home.html', {'trading_pairs': trading_pair, "binance_app_form_choice": binanceappformchoice})
