from django_filters.rest_framework import DjangoFilterBackend


class NameFilter(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(name__isnull=False)
