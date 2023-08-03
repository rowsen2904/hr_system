from django_filters import rest_framework as filters

from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import WorkerFilter
from .models import Worker
from .paginations import WorkerPagination
from .permissions import IsSuperUser, IsSuperUserOrReadOnly
from .serializers import WorkerAllFieldSerializer, WorkerListSerializer


class WorkerListAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WorkerFilter
    permission_classes = [IsAdminUser]


class WorkerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerAllFieldSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    def delete(self, request, pk, fromat=None):
        worker = self.get_object()
        worker.set_as_deleted()
        return Response(status=status.HTTP_200_OK)


class WorkerCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkerAllFieldSerializer
    permission_classes = [IsSuperUser]
