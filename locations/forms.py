from django import forms
from .models import UserReview

ACCESSIBLITY_CHOICES = (
    ("wheelchair", "Wheelchair"),
    ("handrail", "Handrail"),
    ("tactile_paving", "Tactile Paving"),
    ("accessible_parking", "Accessible Parking"),
    ("accessible_restroom", "Accessible Restroom"),
)


class UserReviewForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = UserReview
        fields = ("correct_info",)


class LocationCreateForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter the name of the location",
            }
        ),
    )

    latitude = forms.FloatField(
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter the latitude of the location",
            }
        ),
    )

    longitude = forms.FloatField(
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter the longitude of the location",
            }
        ),
    )

    category = forms.Field(
        widget=forms.Select(
            {"placeholder": "Select Category Type", "class": "select is-fullwidth"},
            choices=ACCESSIBLITY_CHOICES,
        )
    )
