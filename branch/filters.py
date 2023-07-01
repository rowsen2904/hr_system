from django.contrib.postgres.search import SearchQuery, SearchVector

from django_filters import rest_framework as filters

from .models import Department


class DepartmentFilter(filters.FilterSet):
    branch = filters.CharFilter(field_name="branches__id", lookup_expr="in")
    q = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, _, value):
        search_vector = SearchVector("name")
        search_query = SearchQuery(value)
        return (
            queryset.annotate(search=search_vector)
            .filter(search=search_query)
        )

    class Meta:
        model = Department
        fields = "__all__"
