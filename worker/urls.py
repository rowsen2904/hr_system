from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.ListWorkerAPIView.as_view(), name="wokers-list"),
    path("workers/<str:pk>", views.DetailWorkerView.as_view(), name="workers-detail"),
    path("workers/create/", views.CreateWorkerAPIView.as_view(), name="workers-create"),
    path("workers/status/<str:pk>", views.StatusFilterWorkerListAPIView.as_view(), name="workers-status-filter-list"),
    path("workers/branch/<str:pk>", views.WorkerBranchView.as_view(), name="workers-by-branch"),
]
