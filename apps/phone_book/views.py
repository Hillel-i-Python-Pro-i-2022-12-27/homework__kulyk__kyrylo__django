from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from apps.phone_book.models import Contact


class ContactListView(ListView):
    model = Contact
    template_name = "phone_book/contact_list.html"
    queryset = Contact.objects.all().order_by("-modified_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Contacts List"
        return context


class ContactDetailView(DetailView):
    model = Contact

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Details Contact"
        return context


@method_decorator(login_required, name="dispatch")
class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone_number",
        "avatar",
        "is_auto_generated",
    )
    success_url = reverse_lazy("phone_book:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Contact"
        return context


@method_decorator(login_required, name="dispatch")
class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone_number",
        "avatar",
        "is_auto_generated",
    )
    success_url = reverse_lazy("phone_book:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Contact"
        return context


@method_decorator(login_required, name="dispatch")
class ContactDeleteView(DeleteView):
    model = Contact

    success_url = reverse_lazy("phone_book:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Contact"
        return context
