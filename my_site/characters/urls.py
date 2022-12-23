from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('characters',views.CharactersView, basename="characters")
# router.register('alldata',views.get_all_character_data, basename='alldata')
router.register('all_character_data',views.AllCharacterDataView, basename="all_character_data")

urlpatterns = [
    path('',include(router.urls)),
]
