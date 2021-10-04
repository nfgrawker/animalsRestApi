from rest_framework import generics

from animals.models import Species
from animals.serializers import SpeciesSerializer


class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species-list'


class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species'