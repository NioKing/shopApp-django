from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore


@api_view(['GET'])
def getData(request):
    data = {'test': 123}
    return Response(data)