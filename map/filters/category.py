from collections import defaultdict

from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend

from map.models import OSMPoint


class CategoryFilter(BaseFilterBackend):
    ALLOWED_CATEGORIES = ["leisure", "shop", "religion"]

    def get_categories(self, request) -> list:
        """
        Returns a list of categories.
        """
        categories = request.query_params.get("category", "")
        if not categories:
            raise APIException(detail="Category is required")
        return categories.strip().split(",")

    def filter_queryset(self, request, queryset, view) -> dict[str, list[OSMPoint]]:
        points_by_category = defaultdict(list)
        for category in self.get_categories(request):
            if category not in self.ALLOWED_CATEGORIES:
                raise APIException(
                    detail="Category is not allowed, choose one of %s"
                    % ", ".join(self.ALLOWED_CATEGORIES)
                )
            filter_dict = {
                f"{category}__isnull": False,
                "name__isnull": False,
            }
            points_by_category[category] = queryset.filter(**filter_dict)

        return points_by_category
