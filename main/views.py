from .models import InventoryData
from .serializers import InventorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

class InventoryListCreate(APIView):
    """
    List all computer data, or create a new data.
    """
    
    def get(self, request, format=None):
        snippets = InventoryData.objects.all()
        serializer = InventorySerializer(snippets, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(method="post", request_body=InventorySerializer())
    @action(methods=["post"], detail=True)
    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)