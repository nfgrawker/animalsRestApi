"""Route the specific animal requests."""

from django.urls import path
from animals import views

urlpatterns = [
    path('animals-list/<str:model>/', views.animal_list),
    path('animal/<str:model>/<int:pk>/', views.animal),
]