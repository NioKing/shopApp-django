from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CartSerializer
from .models import Cart

@api_view(['GET'])
def get_cart_data(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({"Cart not found!"}, 404)

