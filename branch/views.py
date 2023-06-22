from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .serializers import BranchSerializer, DepartmentSerializer
from .models import Branch, Department


class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetailDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Branch, id=pk)

    def get(self, request, pk, format=None):
        branch = self.get_object(pk=pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        branch = self.get_object(pk=pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
