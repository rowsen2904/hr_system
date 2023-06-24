from django.urls import path

from . import views

urlpatterns = [
    path("branch/", views.BranchListAPIView.as_view(), name="branch-list"),
    path("branch/create/", views.BranchCreateAPIView.as_view(), name="branch-create"),
    path("branch/<str:pk>", views.BranchDetailAPIView.as_view(), name="branch-detail"),
    path("department/", views.DepartmentListAPIView.as_view(), name="department-list"),
    path("department/create/", views.DepartmentCreateAPIView.as_view(), name="department-create"),
    path("department/<str:pk>", views.DepartmentDetailAPIView.as_view(), name="department-detail"),
]
