from rest_framework import generics

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-list'


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal'
