from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Worker
from .paginations import WorkerPagination
from .serializers import WorkerCreateDetailSerializer, WorkerListSerializer


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer


class WorkerDetailDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Worker, id=pk)

    def get(self, request, pk, fromat=None):
        worker = self.get_object(pk=pk)
        serializer = WorkerCreateDetailSerializer(worker)
        return Response(serializer.data)

    def delete(self, request, pk, fromat=None):
        worker = self.get_object(pk=pk)
        worker.set_as_deleted()
        return Response(status=status.HTTP_200_OK)


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerCreateDetailSerializer


class WorkerBranchView(generics.ListAPIView):
    """ Getting worker by branch ID """
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        branch_id = self.kwargs.get("pk")
        queryset = Worker.objects.filter(branch=branch_id, status="active")
        return queryset


class DeletedWorkerList(generics.ListAPIView):
    queryset = Worker.objects.filter(status="deleted")
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer


class ActiveWorkerList(generics.ListAPIView):
    queryset = Worker.objects.filter(status="active")
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer
