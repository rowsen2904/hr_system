from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Worker
from .paginations import WorkerPagination
from .serializers import WorkerSerializer


class WorkerList(generics.ListAPIView):
    queryset = Worker.objects.all()
    pagination_class = WorkerPagination
    serializer_class = WorkerSerializer
    permission_classes = [IsAuthenticated]


class WorkerBranch(generics.ListAPIView):
    pagination_class = WorkerPagination
    serializer_class = WorkerSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        print(pk)
        return Worker.objects.all()
        
    