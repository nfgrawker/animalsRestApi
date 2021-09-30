"""Parse requests that come in to the Animals routes."""

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Region, Location, Animal, Species
from animals.serializers import RegionSerializer, LocationSerializer, AnimalSerializer, SpeciesSerializer

MODEL_SWITCH_CASE = {"region": (Region, RegionSerializer),
                     "location": (Location, LocationSerializer),
                     "animal": (Animal, AnimalSerializer),
                     "species": (Species, SpeciesSerializer)}



class ModelList(APIView):
    """
    List all of one model, or create a models from a list.
    """

    def get_model(self, model):
        _model, _serializer = MODEL_SWITCH_CASE[model]
        return _model, _serializer

    def get(self, request, format=None):
        model = self.request.query_params.get("model")
        _model, _serializer = self.get_model(model)
        model_data = _model.objects.all()
        serializer = _serializer(model_data, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request, format=None):
        model = self.request.query_params.get("model")
        _, _serializer = self.get_model(model)
        serializer = _serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelDetail(APIView):
    """
    Retrieve, update or delete a model instance.
    """

    def get_model(self, model):
        model, serializer = MODEL_SWITCH_CASE[model]
        return model, serializer

    def get_object(self, model, serializer, pk):
        try:
            return model.objects.get(pk=pk)
        except serializer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        model = self.request.query_params.get("model")
        _model, _serializer = self.get_model(model)

        model_data = self.get_object(_model, _serializer, pk)
        serializer = _serializer(model_data)
        return Response(serializer.data)
    @csrf_exempt
    def put(self, request, pk, format=None):
        model = self.request.query_params.get("model")
        _model, _serializer = self.get_model(model)

        model_data = self.get_object(_model, _serializer, pk)
        serializer = _serializer(model_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @csrf_exempt
    def delete(self, request, pk, format=None):
        model = self.request.query_params.get("model")
        _model, _serializer = self.get_model(model)

        model_data = self.get_object(_model, _serializer, pk)
        model_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
