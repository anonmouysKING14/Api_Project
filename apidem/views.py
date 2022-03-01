from django.http import JsonResponse, response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
@api_view(['GET'])
def apiCreated(request):
    return Response(" Lets Do It")
@api_view(['POST'])
def UserCreated(request):
    serializer=TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
