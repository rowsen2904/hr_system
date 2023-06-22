from django.urls import path

from . import views

urlpatterns = [
    path("branch/", views.BranchListCreateView.as_view(), name="branch-list-create"),
    path("branch/<str:pk>", views.BranchDetailDeleteView.as_view(), name="branch-detail-delete"),
    path("department/", views.DepartmentCreateView.as_view(), name="department-create")
]
