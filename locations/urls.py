from django.urls import path

from locations.views import MapView

urlpatterns = [
    path("", MapView.as_view(), name="map"),
]
