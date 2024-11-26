from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import generics
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

    def list(self, request, *args, **kwargs):
        cache_key = 'animals-list'
        cache_time = 60 * 5
        data = cache.get(cache_key)

        if not data:
            animals = Animal.objects.all()
            data = AnimalSerializer(animals, many=True).data
            cache.set(cache_key, data, cache_time)

        return Response(data)

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer