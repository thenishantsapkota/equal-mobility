from django.db import models

ACCESSIBLITY_CHOICES = (
    ("wheelchair", "Wheelchair"),
    ("handrail", "Handrail"),
    ("tactile_paving", "Tactile Paving"),
)


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class AccessibilityFeature(models.Model):
    category = models.CharField(max_length=25, choices=ACCESSIBLITY_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.category}({self.location.latitude}, {self.location.longitude})"
