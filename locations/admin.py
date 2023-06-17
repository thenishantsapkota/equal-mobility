from django.contrib import admin
from locations.models import Location, AccessibilityFeature

# Register your models here.

admin.site.register(Location)
admin.site.register(AccessibilityFeature)
