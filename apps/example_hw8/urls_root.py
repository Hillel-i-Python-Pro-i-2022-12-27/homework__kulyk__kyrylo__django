from django.urls import path

from apps.example_hw8 import views

app_name = "root"

urlpatterns = [
    path("", views.index, name="index"),
]
