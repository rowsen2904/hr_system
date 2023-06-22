from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.WorkerListView.as_view(), name="wokers-list"),
    path("workers/create/", views.WorkerCreateView.as_view(), name="workers-create"),
    path("workers/active/", views.ActiveWorkerList.as_view(), name="active-wokers-list"),
    path("workers/deleted/", views.DeletedWorkerList.as_view(), name="deleted-wokers-list"),
    path("workers/<str:pk>", views.WorkerDetailDeleteView.as_view(), name="workers-detail-delete"),
    path("workers/branch/<str:pk>", views.WorkerBranchView.as_view(), name="workers-by-branch"),
]
