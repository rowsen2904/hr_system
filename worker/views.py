from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Worker
from .paginations import WorkerPagination
from .serializers import WorkerAllFieldSerializer, WorkerListSerializer


class ListWorkerAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    
class DetailWorkerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerAllFieldSerializer
    
    def delete(self, request, pk, fromat=None):
        worker = self.get_object()
        worker.set_as_deleted()
        return Response(status=status.HTTP_200_OK)


class CreateWorkerAPIView(generics.CreateAPIView):
    serializer_class = WorkerAllFieldSerializer


class WorkerBranchView(generics.ListAPIView):
    """ Getting worker by branch ID """
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        branch_id = self.kwargs.get("pk")
        queryset = Worker.objects.filter(branch=branch_id, status="active")
        return queryset


class StatusFilterWorkerListAPIView(generics.ListAPIView):
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        queryset = Worker.objects.filter(status=pk)
        return queryset
