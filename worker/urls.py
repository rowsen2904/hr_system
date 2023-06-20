from django.urls import path

from . import views

urlpatterns = [
    path("", views.WorkerList.as_view())
]
