from django.urls import path

from . import views

app_name = "count_of_visits"

urlpatterns = [
    path("", views.CountOfVisitsView.as_view(), name="index"),
]
