"""Parse requests that come in to the Animals routes."""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from animals.sevices.animals_service import AnimalList
from animals.sevices.location_service import LocationList
from animals.sevices.species_service import SpeciesList
from animals.sevices.region_service import RegionList


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'animals': reverse(AnimalList.name, request=request), 'location': reverse(LocationList.name, request=request), 'species': reverse(SpeciesList.name, request=request), 'region': reverse(RegionList.name, request=request)})
