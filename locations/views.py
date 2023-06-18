from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import AccessibilityFeature, Location, UserReview
from .forms import LocationCreateForm, UserReviewForm


# Create your views here.
class MapView(View):
    form = UserReviewForm

    def get(self, request):
        form = self.form()
        if request.user.is_authenticated:
            reviews = UserReview.objects.filter(user=request.user)
        else:
            reviews = []

        features = AccessibilityFeature.objects.all()
        return render(
            request,
            "locations/map.html",
            {
                "features": features,
                "form": form,
                "reviews": reviews,
            },
        )


class AccessibilityFeatureView(View):
    form = UserReviewForm

    def post(self, request, pk):
        feature = AccessibilityFeature.objects.get(id=pk)
        form = self.form(request.POST)
        if UserReview.objects.filter(
            accessibility_feature=feature, user=request.user
        ).exists():
            messages.error(request, "You have already reviewed this location")
            return redirect("/")
        review = form.save(commit=False)
        location = Location.objects.get(accessibilityfeature=feature)
        if name := form.cleaned_data.get("name"):
            location.name = name
            location.save()
        if review.correct_info:
            review.positive_reviews += 1
        else:
            review.negative_reviews += 1
        review.user = request.user
        review.accessibility_feature = feature
        review.save()
        messages.success(request, "Review added successfully!")
        return redirect("/")


class AccessibilityAddView(View):
    form = LocationCreateForm

    def get(self, request):
        lat = request.GET.get("lat")
        lng = request.GET.get("lng")

        data = {"latitude": lat, "longitude": lng}
        form = self.form(data=data)

        return render(request, "locations/add_location.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            location, created = Location.objects.get_or_create(
                name=form.cleaned_data.get("name"),
                latitude=form.cleaned_data.get("latitude"),
                longitude=form.cleaned_data.get("longitude"),
            )

            (
                accessibility_feature,
                isCreated,
            ) = AccessibilityFeature.objects.get_or_create(
                location=location, category=form.cleaned_data.get("category")
            )

            messages.success(request, "Location added successfully!")
            return redirect("/")
        return render(
            request,
            "locations/add_location.html",
            {
                "form": form,
            },
        )
