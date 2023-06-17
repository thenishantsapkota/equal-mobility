from django.urls import path

from locations.views import MapView, AccessibilityFeatureView, AccessibilityAddView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", MapView.as_view(), name="map"),
    path(
        "add-review/<pk>/",
        login_required(AccessibilityFeatureView.as_view(), login_url="/auth/login/"),
        name="add-review",
    ),
    path(
        "create-location/",
        login_required(AccessibilityAddView.as_view(), login_url="/auth/login/"),
        name="add-location",
    ),
]
