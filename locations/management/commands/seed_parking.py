import overpy
from django.core.management.base import BaseCommand
from locations.models import AccessibilityFeature, Location


class Command(BaseCommand):
    help = "Fetches accessible parking related data in Django Models"

    def handle(self, *args, **kwargs):
        api = overpy.Overpass()

        query = """
        [out:json][timeout:25];
        area(id:3600184633)->.searchArea;
        (
        node["parking"]["access"="yes"](area.searchArea);
        way["parking"]["access"="yes"](area.searchArea);
        relation["parking"]["access"="yes"](area.searchArea);
        );
        out center;
        """
        result = api.query(query)
        i = 0

        for element in result.nodes + result.ways + result.relations:
            if i == 100:
                break
            if isinstance(element, overpy.Node):
                latitude = element.lat
                longitude = element.lon
            elif isinstance(element, overpy.Way):
                latitude = element.center_lat
                longitude = element.center_lon
            elif isinstance(element, overpy.Relation):
                continue
            else:
                continue

            name = element.tags.get("name", "")  # type: ignore
            accessibility_feature = "accessible_parking"

            location, created = Location.objects.get_or_create(
                latitude=latitude, longitude=longitude, defaults={"name": name}
            )

            (
                accessibility_feature_obj,
                feature_created,
            ) = AccessibilityFeature.objects.get_or_create(
                category=accessibility_feature, location=location
            )

            if not feature_created:
                accessibility_feature_obj.category = accessibility_feature
                accessibility_feature_obj.save()

            i += 1

        self.stdout.write(self.style.SUCCESS("Data stored successfully."))
