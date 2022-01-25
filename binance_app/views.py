from . import main
from rest_framework.response import Response
from rest_framework.decorators import api_view
from binance_app.src.log import Log
from datetime import datetime


@api_view(('GET',))
def exe(request):
    if request.method == 'GET':

        logging_v_ip(request)

        body = request.data

        data = main.main(param={"trading pair": body['trading pair']})

        return Response(data)
    return


def logging_v_ip(request):
    log = Log("exe view")

    log.set_warning_msg(
        "\U0001F600 - exe() view CALLED AT %s" % datetime.now()
        .strftime("%Y-%m-%d %I:%M:%S %z"))

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        v_ip = x_forwarded_for.split(',')[0]
    else:
        v_ip = request.META.get('REMOTE_ADDR')

    log.set_warning_msg("\U0001F600 - exe() view called by %s"
                        % str(v_ip))
