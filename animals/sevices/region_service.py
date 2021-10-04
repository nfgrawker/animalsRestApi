from rest_framework import generics

from animals.models import Region
from animals.serializers import RegionSerializer


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    name = 'region-list'


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    name = 'region'
