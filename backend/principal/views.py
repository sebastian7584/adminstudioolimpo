from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer

# Create your views here.

def cargarChaturbate(request):
    earning = Country(
        date = '8',
        id_account = '9999',
        amount = 50.20,
        id_period = 2023091
    )
    earning.save()

@api_view(["GET", "POST", "PUT"])
def createCountry(request):

    if request.method == "GET":
        return Response({'a':'get'})

    if request.method == "POST":
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        return Response({'a':'put'})