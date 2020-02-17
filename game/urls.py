from django.urls import path
from .views import LaunchView, game_view

urlpatterns = [
    path('', LaunchView.as_view(), name="LaunchView"),
    path('fight', game_view, name="game")
]
