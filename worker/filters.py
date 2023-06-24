from django_filters import rest_framework as filters

from .models import Worker


class WorkerFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status")
    department = filters.CharFilter(field_name="department")

    class Meta:
        model = Worker
        fields = ["status", "department"]
