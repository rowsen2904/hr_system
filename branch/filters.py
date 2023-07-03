from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django_filters import rest_framework as filters

from .models import Department


class DepartmentFilter(filters.FilterSet):
    branch = filters.CharFilter(field_name="branches__id", lookup_expr="in")
    q = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Department
        fields = ["branch", "q"]
