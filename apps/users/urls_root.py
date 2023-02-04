from django.urls import path

from apps.users import views

app_name = "root"

urlpatterns = [
    path("", views.index, name="index"),
]
