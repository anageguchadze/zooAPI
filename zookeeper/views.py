from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
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
    
class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    @action(detail=False, methods=['post'])
    def mark_endangered(self, request):
        ids = request.data.get('ids', [])
        animals = Animal.objects.filter(id__in=ids)

        animals.update(status='endangered')

        return Response({'status': 'marked as endangered'}, status=status.HTTP_200_OK)