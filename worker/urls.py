from django.urls import path

from . import views

urlpatterns = [
    path("", views.WorkerList.as_view()),
    path("test/<str:pk>", views.WorkerBranch.as_view()),
]
