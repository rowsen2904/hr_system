from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.WorkerListView.as_view(), name="wokers-list"),
    path("workers/create/", views.WorkerCreateView.as_view(), name="workers-create"),
    path("workers/detail/<str:pk>", views.WorkerDetailView.as_view(), name="workers-detail"),
    path("workers/branch/<str:pk>", views.WorkerBranchView.as_view(), name="workers-by-branch"),
]
