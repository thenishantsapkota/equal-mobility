from django.db import models
from django.conf import settings

ACCESSIBLITY_CHOICES = (
    ("wheelchair", "Wheelchair"),
    ("handrail", "Handrail"),
    ("tactile_paving", "Tactile Paving"),
    ("accessible_parking", "Accessible Parking"),
    ("accessible_restroom", "Accessible Restroom"),
)


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


class AccessibilityFeature(models.Model):
    category = models.CharField(max_length=25, choices=ACCESSIBLITY_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category}({self.location.latitude}, {self.location.longitude})"


class UserReview(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    accessibility_feature = models.ForeignKey(
        AccessibilityFeature,
        on_delete=models.CASCADE,
    )
    correct_info = models.BooleanField(default=True)
    positive_reviews = models.PositiveIntegerField(default=0)
    negative_reviews = models.PositiveIntegerField(default=0)
