"""Turn JSON bytes to Python and Back again."""
from rest_framework import serializers

from animals.models import Region, Location, Species, Animal


class RegionSerializer(serializers.ModelSerializer):
    """Serialize the Region Model."""

    class Meta:
        model = Region
        fields = ["id", "name", "location", "coordinates", ]


class LocationSerializer(serializers.ModelSerializer):
    """Serialize the Location Model."""

    class Meta:
        model = Location
        fields = ["id", "name", "zip_code", ]


class SpeciesSerializer(serializers.ModelSerializer):
    """Serialize the Species Model."""

    class Meta:
        model = Species
        fields = ["id", "name", "region", "wiki_url", ]


class AnimalSerializer(serializers.ModelSerializer):
    """Serialize the Animal Model."""

    class Meta:
        model = Animal
        fields = ["id", "first_name", "last_name", "location", ]
