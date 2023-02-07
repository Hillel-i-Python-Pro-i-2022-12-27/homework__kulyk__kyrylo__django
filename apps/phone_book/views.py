from django.urls import reverse_lazy
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
        return super().get_context_data(**kwargs)


class ContactCreateView(CreateView):
    model = Contact
    fields = (
        "name",
        "phone_number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("phone_book:list")


class ContactUpdateView(UpdateView):
    model = Contact
    fields = (
        "id",
        "name",
        "phone_number",
        "is_auto_generated",
    )
    success_url = reverse_lazy("phone_book:list")


class ContactDeleteView(DeleteView):
    model = Contact

    success_url = reverse_lazy("phone_book:list")
