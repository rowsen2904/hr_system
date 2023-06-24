from django_filters import rest_framework as filters

from .models import Department


class DepartmentFilter(filters.FilterSet):
    branch = filters.CharFilter(field_name="branches__id", lookup_expr="in")

    class Meta:
        model = Department
        fields = "__all__"
