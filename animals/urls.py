"""Route the specific animal requests."""

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from animals import views
from animals.sevices.animals_service import AnimalList, AnimalDetail
from animals.sevices.location_service import LocationList, LocationDetail
from animals.sevices.region_service import RegionList, RegionDetail
from animals.sevices.species_service import SpeciesList, SpeciesDetail

urlpatterns = format_suffix_patterns([
    path('animal/<int:pk>/', AnimalDetail.as_view(), name=AnimalDetail.name),
    path('animal-list', AnimalList.as_view(), name=AnimalList.name),
    path('location/<int:pk>/', LocationDetail.as_view(), name=LocationDetail.name),
    path('location-list', LocationList.as_view(), name=LocationList.name),
    path('region/<int:pk>/', RegionDetail.as_view(), name=RegionDetail.name),
    path('region-list', RegionList.as_view(), name=RegionList.name),
    path('species/<int:pk>/', SpeciesDetail.as_view(), name=SpeciesDetail.name),
    path('species-list', SpeciesList.as_view(), name=SpeciesList.name),
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name)
])
