from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BenefactorSerializer, CharitySerializer
from .models import Benefactor, Charity

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
