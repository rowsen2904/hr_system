from django_filters import rest_framework as filters

from rest_framework import generics

from .filters import DepartmentFilter
from .serializers import BranchSerializer, DepartmentSerializer
from .models import Branch, Department


class BranchListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchCreateAPIView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DepartmentFilter


class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateAPIView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
