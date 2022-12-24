from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters',views.CharactersView, basename="characters")
router.register('all_character_data',views.AllCharacterDataView, basename="all_character_data")
router.register('calculate_matchup',views.CalculateMatchUpView, basename="calculate_matchup")

urlpatterns = [
    path('',include(router.urls)),
]
