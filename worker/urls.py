from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.WorkerListAPIView.as_view(), name="wokers-list"),
    path("workers/<str:pk>/",
         views.WorkerDetailAPIView.as_view(), name="workers-detail"),
    path("workers/create/",
         views.WorkerCreateAPIView.as_view(), name="workers-create"),
]
