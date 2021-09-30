"""Stores our database models."""

# Todo - Convert to using this import and geolocator data in the future when we migrate to postgres.
# from django.contrib.gis.db import models as gis_models
from django.db import models

from validators.string_validation import no_naughty_words


class Region(models.Model):
    """Store Natural location of Species."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default="Unknown")
    # Todo - This will become gis_models.PolygonField
    coordinates = models.CharField(default=None, max_length=12)

    class Meta:
        ordering = ['created']


class Location(models.Model):
    """Store Specific Location of Animal."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default="Unknown")
    zip_code = models.CharField(max_length=10, default="Unknown")

    class Meta:
        ordering = ['created']


class Species(models.Model):
    """Store data about species of Individual Animals."""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(unique=True, max_length=50)
    region = models.ForeignKey(Region, default=None, on_delete=models.SET_NULL, null=True)
    wiki_url = models.CharField(max_length=100, default="Unknown")

    class Meta:
        ordering = ['created']


class Animal(models.Model):
    """Store Animal data."""
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, validators=[no_naughty_words])
    last_name = models.CharField(max_length=30, validators=[no_naughty_words])
    location = models.ForeignKey(Location, default=None, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['created']
