from django.shortcuts import render
from django.views import View
from .models import AccessibilityFeature


# Create your views here.
class MapView(View):
    def get(self, request):
        features = AccessibilityFeature.objects.all()
        return render(request, "locations/map.html", {"features": features})
