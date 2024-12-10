import enum

from django.db.models import TextChoices
from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend
from rest_framework.views import APIView


class OSMCategoryEnum(TextChoices):
    leisure = "leisure"
    shop = "shop"
    religion = "religion"


ALLOWED_CATEGORIES = ["leisure", "shop", "religion"]


class CategoryFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category = request.query_params.get("category", None)
        if not category:
            raise APIException(detail="Category is required")

        if category not in ALLOWED_CATEGORIES:
            raise APIException(
                detail="Category is not allowed, choose one of %s"
                % ", ".join(ALLOWED_CATEGORIES)
            )

        filter_dict = {
            f"{category}__isnull": False,
        }

        return queryset.filter(**filter_dict)
