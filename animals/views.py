"""Parse requests that come in to the Animals routes."""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Region, Location, Animal, Species
from animals.serializers import RegionSerializer, LocationSerializer, AnimalSerializer, SpeciesSerializer

MODEL_SWITCH_CASE = {"region": (Region, RegionSerializer),
                     "location": (Location, LocationSerializer),
                     "animal": (Animal, AnimalSerializer),
                     "species": (Species,SpeciesSerializer)}

class ModelList(APIView):
    """
    List all of one model, or create a models from a list.
    """
    def get_model(self, model):
        model, serializer = MODEL_SWITCH_CASE[model]
        return model,serializer

    def get(self, request,model, format=None):
        _model,_serializer = self.get_model(model)
        snippets = _model.objects.all()
        serializer = _serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, model,format=None):
        _,_serializer = self.get_model(model)
        serializer = _serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)