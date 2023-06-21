from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Worker
from .paginations import WorkerPagination
from .serializers import WorkerCreateSerializer, WorkerListSerializer


class WorkerList(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer


class WorkerCreate(generics.CreateAPIView):
    serializer_class = WorkerCreateSerializer


class WorkerBranch(generics.ListAPIView):
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        branch_id = self.kwargs.get("pk")
        queryset = Worker.objects.filter(branch=branch_id)
        return queryset
