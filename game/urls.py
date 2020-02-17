from django.urls import path
from .views import LaunchView

urlpatterns = [
    path('', LaunchView.as_view(), name="LaunchView")
]
