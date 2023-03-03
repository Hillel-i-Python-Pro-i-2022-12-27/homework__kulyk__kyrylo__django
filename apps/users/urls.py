from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("registration/", views.RegisterFormView.as_view(), name="registration"),
    path("details/<int:pk>", views.UserDetailView.as_view(), name="details"),
    path("update/<int:pk>", views.UserUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.UserDeleteView.as_view(), name="delete"),
]
