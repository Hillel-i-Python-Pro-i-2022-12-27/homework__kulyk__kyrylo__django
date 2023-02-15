from django.urls import path

from . import views

app_name = "example_hw8"

urlpatterns = [
    path("<int:amount>", views.UsersView.as_view(), name="users_with_amount"),
    path("", views.UsersView.as_view(), name="users_with_amount"),
]
