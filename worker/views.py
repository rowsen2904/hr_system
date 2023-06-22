from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Worker
from .paginations import WorkerPagination
from .serializers import WorkerCreateSerializer, WorkerListSerializer


class WorkerListView(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer
    
    
class WorkerDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Worker, id=pk)

    def get(self, request, pk, fromat=None):
        worker = self.get_object(pk=pk)
        serializer = WorkerCreateSerializer(worker)
        return Response(serializer.data)


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerCreateSerializer


class WorkerBranchView(generics.ListAPIView):
    pagination_class = WorkerPagination
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        branch_id = self.kwargs.get("pk")
        queryset = Worker.objects.filter(branch=branch_id)
        return queryset
