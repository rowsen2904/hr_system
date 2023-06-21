from django.urls import path

from . import views

urlpatterns = [
    path("workers/", views.WorkerList.as_view()),
    path("workers/create/", views.WorkerCreate().as_view()),
    path("workers/branch/<str:pk>", views.WorkerBranch.as_view()),
]
