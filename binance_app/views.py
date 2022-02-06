import hashlib
from binance_app import main
from rest_framework.response import Response
from rest_framework.decorators import api_view
from binance_app.src.log import Log
from datetime import datetime
from django.shortcuts import render, redirect
from binance_app.models import TradingPair


@api_view(('GET',))
def exe(request):
    if request.method == 'GET':

        logging_v_ip(request)

        body = request.data

        data = main.main(param={"trading pair": body['trading pair']})

        return Response(data)
    return


def execute_new_req(request):
    logging_v_ip(request)
    main.main()
    return redirect('home')


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
    # https://docs.djangoproject.com/en/4.0/topics/db/queries/#limiting-querysets
    trading_pair = TradingPair.objects.all().order_by('-api_dt')[:5]
    return render(request, 't_b_app/home.html', {'trading_pair': trading_pair})
