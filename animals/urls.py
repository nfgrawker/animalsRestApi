"""Route the specific animal requests."""

from django.urls import path
from animals import views

urlpatterns = [
    path('animals-list', views.ModelList.as_view()),
    path('animal/<int:pk>/', views.ModelDetail.as_view()),
]