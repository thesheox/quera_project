from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from charities.models import Charity, Benefactor
from .serializers import BenefactorSerializer, CharitySerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['POST'])
def BenefactorRegistration(request):
    if request.method == 'POST':
        serializer = BenefactorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CharityRegistration(request):
    if request.method == 'POST':
        serializer = CharitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )



class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = UserSerializer


class BenefactorRegistration(generics.CreateAPIView):
    queryset = Benefactor.objects.all()
    serializer_class = BenefactorSerializer

    def perform_create(self, serializer):
        BenefactorSerializer.save(user=self.request.user)


class CharityRegistration(generics.CreateAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer

    def CharitySerializer(self, serializer):
        serializer.save(user=self.request.user)