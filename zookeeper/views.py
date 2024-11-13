from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategotyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalBatchDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', [])

        if not ids:
            return Response({'error': 'NO IDS PROVIDED'}, status=status.HTTP_400_BAD_REQUEST)

        Animal.objects.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)