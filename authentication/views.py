from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# @api_view(["POST"])
# def login(request):
#     return Response({"message": "Login"})

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_user_data(request, pk):
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)


