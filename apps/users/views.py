from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView, DeleteView

from apps.users.forms import UserRegisterForm

User = get_user_model()


class RegisterFormView(FormView):
    form_class = UserRegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("root:index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("root:index")


class UserDetailView(DetailView):
    model = User
    template_name = "users/details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Details User"
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/update.html"
    fields = ("username", "email", "first_name", "last_name", "avatar")
    success_url = reverse_lazy("root:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Details User"
        return context


class UserDeleteView(DeleteView):
    model = User

    success_url = reverse_lazy("root:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Account"
        return context
