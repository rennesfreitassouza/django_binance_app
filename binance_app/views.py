from . import main
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET',))
def exe(request):
    if request.method == 'GET':

        body = request.data

        data = main.main(param={"trading pair": body['trading pair']})

        return Response(data)
    return
