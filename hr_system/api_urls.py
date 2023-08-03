from django.urls import path, include

urlpatterns = [
    path("", include("worker.urls")),
    path("", include("branch.urls")),
]