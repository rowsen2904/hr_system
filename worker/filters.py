from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from django_filters import rest_framework as filters

from .models import Worker


class WorkerFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status")
    gender = filters.CharFilter(field_name="gender")
    department = filters.CharFilter(field_name="department")
    q = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, _, value):
        search_vector = (
            SearchVector("fullname", weight="A")
            + SearchVector("id", weight="B")
            + SearchVector("emp_number", weight="C")
        )
        search_query = SearchQuery(value)
        search_rank = SearchRank(search_vector, search_query)
        return (
            queryset.annotate(search=search_vector, rank=search_rank)
            .filter(search=search_query)
            .order_by("-rank")
        )
        

    class Meta:
        model = Worker
        fields = ["status", "department"]
