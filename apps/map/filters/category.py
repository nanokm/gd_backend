from collections import defaultdict

from django.db.models import Q
from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend
from rest_framework.request import Request

from apps.map.models import OSMPoint


class CategoryFilter(BaseFilterBackend):
    ALLOWED_CATEGORIES = ["leisure", "shop", "religion"]

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
                detail="Invalid category queryparam=%s. Choose from %s" % (r, ", ".join(self.ALLOWED_CATEGORIES))
            )

        q = Q()
        for category in categories:
            q |= Q(**{f"{category}__isnull": False})

        qs = queryset.filter(q)
        qs = qs.filter(name__isnull=False)
        return qs
