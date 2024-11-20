from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from .serializers import UserSerializer
from .models import User

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        try:
            user = User.objects.create_user(email=email, password=password)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=201)
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


@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)