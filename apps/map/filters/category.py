from django.conf import settings
from django.db.models import Q
from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request

from apps.map.models import OSMPoint


class CategoryFilter(BaseFilterBackend):
    ALLOWED_CATEGORIES = settings.OSM_CATEGORY_LIST
    OSM_MAPPING = settings.OSM_CATEGORY_MAPPING

    def get_categories(self, request: Request) -> list:
        """
        Returns a list of categories.
        """
        categories = request.query_params.get("category", "")
        if not categories:
            raise APIException(detail="Category queryparam is required.")
        return categories.strip().split(",")

    def filter_queryset(self, request, queryset, view) -> dict[str, list[OSMPoint]]:
        categories = self.get_categories(request)
        if any(r := set(categories) - set(self.ALLOWED_CATEGORIES)):
            raise APIException(
                detail="Invalid category queryparam=%s. Choose from: %s" % (r, ", ".join(self.ALLOWED_CATEGORIES))
            )

        q = Q()
        for category in categories:
            selected_category_mapping = self.OSM_MAPPING[category]
            if isinstance(selected_category_mapping, dict):
                column = self.OSM_MAPPING[category]["column"]
                column_value = self.OSM_MAPPING[category]["value"]
                q |= Q(**{f"{column}": column_value})
            elif isinstance(selected_category_mapping, list):
                for filter_elem in selected_category_mapping:
                    column = filter_elem["column"]
                    value = filter_elem["value"]
                    q |= Q(**{f"{column}": value})
        qs = queryset.filter(q)
        return qs
