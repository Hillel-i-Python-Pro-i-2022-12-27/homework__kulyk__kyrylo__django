from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [path("list/", views.ContactListView.as_view(), name="list")]
